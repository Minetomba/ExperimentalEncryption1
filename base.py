import argparse, random, json, base64, os; D="\u2063"; j=json; b=base64; E=Exception; M=lambda m:b.b85encode(j.dumps(m).encode()).decode(); U=lambda h:j.loads(b.b85decode(h)); S=lambda s,i,j:s if i==j else''.join((lambda l:(l.__setitem__(i,s[j]),l.__setitem__(j,s[i]),l)[-1])(list(s)))
def e(s,b):d=0;[d:=d*256+c for c in s.encode()];r=[];exec("r.append(chr(d%b+50));d//=b;"*999);r.reverse();return['2']if not r else r
def d(g,b):v=0;[(v:=v*b+ord(c)-50) if 0<=ord(c)-50<b else (_ for _ in ()).throw(E(f"Digit '{c}' invalid for base {b}")) for c in g];r=[];exec("r.append(v&255);v>>=8;"*999);r.reverse();return''.join(map(chr,r)).strip('\x00')
def main():
 p=argparse.ArgumentParser();a=p.add_argument;a("cmd",choices=["encode","decode"]);a("text");a("base",type=int);a("--mixes");a("--mixes-file");a("--save-mixes-file");args=p.parse_args()
 if args.cmd=="encode":
  z=e(args.text,args.base);s=D.join(z);m=[];l=len(s)
  for _ in range(random.randint(500,1000)):i,j=random.randint(0,l-1),random.randint(0,l-1);m.append([i,j]);s=S(s,i,j)
  print(b.b16encode(s.encode()).decode());f=args.save_mixes_file;open(f,'w').write(M(m)) if f else None
 else:
  z=b.b16decode(args.text).decode().split(D);m=U(open(args.mixes_file).read()) if args.mixes_file and os.path.exists(args.mixes_file) else U(args.mixes) if args.mixes else (_ for _ in ()).throw(E("Need --mixes or --mixes-file"))
  for i,j in reversed(m):z=S(D.join(z),i,j).split(D)
  print(d(z,args.base))
main()
