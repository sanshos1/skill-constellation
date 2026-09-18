import json,re,secrets,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];E=(R.parents[3]/'accounts.env').read_text();key=re.search(r'^ACCOUNT_3_GENLAYER_PRIVATE_KEY="?([^"\r\n]+)',E,re.M).group(1).strip();owner=create_account(account_private_key=key);aa=create_account(account_private_key='0x'+secrets.token_hex(32));ab=create_account(account_private_key='0x'+secrets.token_hex(32));clients=[create_client(chain=studionet,account=x) for x in (owner,aa,ab)];addr='0x8FD589e41c240609a7067F5a5C3AFDE3F5416A4e';item='LIVE-'+str(int(time.time()));base='f9bdb5d';urls=[f'https://github.com/sanshos1/skill-constellation/raw/{base}/evidence/rubric.txt',f'https://raw.githubusercontent.com/sanshos1/skill-constellation/{base}/evidence/assessment-a.txt',f'https://cdn.jsdelivr.net/gh/sanshos1/skill-constellation@{base}/evidence/assessment-b.txt'];tx=[]
def send(cl,fn,args):
 h=cl.write_contract(address=addr,function_name=fn,args=args);r=cl.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';tx.append(h)
send(clients[0],'claim',[item,'Incident facilitation','Facilitate a documented multi-party incident review',aa.address,ab.address,urls[0],2592000]);send(clients[1],'assess',[item,urls[1]]);send(clients[2],'assess',[item,urls[2]]);print(json.dumps({'id':item,'state':'ACTIVE','transactions':tx}),flush=True)
