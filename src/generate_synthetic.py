import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import ks_2samp

def synthesize(df, n, seed=42):
    rng=np.random.default_rng(seed)
    out={}
    for c in df.columns:
        s=df[c]
        if pd.api.types.is_numeric_dtype(s):
            x=pd.to_numeric(s,errors="coerce").dropna().to_numpy()
            if len(x)==0: out[c]=[np.nan]*n; continue
            sampled=rng.choice(x,size=n,replace=True)
            scale=max(float(np.std(x))*0.05, 1e-9)
            vals=sampled+rng.normal(0,scale,size=n)
            vals=np.clip(vals,float(np.min(x)),float(np.max(x)))
            out[c]=vals
        else:
            vals=s.dropna().astype(str)
            if vals.empty: out[c]=[""]*n
            else:
                probs=vals.value_counts(normalize=True)
                out[c]=rng.choice(probs.index.to_numpy(),size=n,p=probs.to_numpy())
    return pd.DataFrame(out)

def compare(real, syn):
    report={"numeric_ks":{}}
    for c in real.columns:
        if c in syn.columns and pd.api.types.is_numeric_dtype(real[c]):
            a=pd.to_numeric(real[c],errors="coerce").dropna()
            b=pd.to_numeric(syn[c],errors="coerce").dropna()
            if len(a) and len(b):
                stat,p=ks_2samp(a,b)
                report["numeric_ks"][c]={"statistic":float(stat),"p_value":float(p)}
    rset=set(map(tuple, real.astype(str).itertuples(index=False,name=None)))
    srows=list(map(tuple, syn.astype(str).itertuples(index=False,name=None)))
    overlap=sum(1 for row in srows if row in rset)
    report["exact_row_overlap_count"]=overlap
    report["exact_row_overlap_percent"]=round(100*overlap/max(len(srows),1),3)
    return report

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv"); ap.add_argument("--rows",type=int,default=1000); ap.add_argument("--output",default="synthetic.csv")
    a=ap.parse_args()
    real=pd.read_csv(a.csv); syn=synthesize(real,a.rows)
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); syn.to_csv(out,index=False)
    print(json.dumps(compare(real,syn),indent=2))

if __name__=="__main__": main()
