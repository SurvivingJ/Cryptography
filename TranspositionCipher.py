import math

message = '''Wutei .lemFcht lo wb(apolaoio pfgl:/g/ /chtksi/sig appntPutlsedduno=e%=ytniatmrgephscrsto,.e oefcwrt/lomilynnndtel l/ a h kiteuc/ts -rlsit8bhyh_ieeonba2o&yctpeekrrhaehf oCr o.cm 'oa h enmc  d)  ocepe/ r tw /sprgapa t ee:mpu.i.eae_&t_or0rfplhrrpeasyt ?lh Tglroh/tsmyse( eiosn (d ialnhhahthCs:sglwrvhw a/esDcrcrssoieaontiaeupenalm.. ivoalF/igrapo,pso ac ncteh oilfragatgtpthi/te nteehss/l:3odo_s=rnbckiroc=dysagemecit=wne  v/glro a mw hogtuwahnfointextet:tat/esbanr eheeb/Im-mdeticoc&naleeetsleyinos)8,dac e /laltrreonaf fd stefwc.fs.p.p/plecntidoywra b//L/e/asroloofgietx_h.._.n.m  e sroU  cec hee rel s.ee t i-aco)tso:/:l.t.envw aerdormtddstsulukuo%n&_psocBbegp/C-vh nmptWtntoedqokwltecnvapocllor o:r/w/eofndaesgt eooeeEaieameedsnr2ifjeanoaad/dcT 9td,pcehfgiry ut eehtote sfuelmm r/g/w/nr.l rntoerdnkagJtta=e&se=tm0nosrn.mnnuRfiFhZto aoaa-eci tihfrnesmsrg: lvy/ h.//wwcggk/bytoore.'cdayairtni=_t=apgrotdc/nn/e p?tXpwacmmtw eetoreo g  / yr/tte  wthp w.oe/oby upd.a tee.3/ocrtntcrfta&mn&bogeepvhh t9:nlti  tw-ne errsemo w e/hylo(ituw wous mi ar)  nrnSpnhuscrouastfa=iomprraete(pJ/ o nsifectat   esof(hyame  natp/nh.vn. on/ne i  tpt.zEy /e=lulel=hottnx// rtrts4/onggcs/btechtpyt)r Dieti cr  h: 0thethhdaua. fawhora/6th?&fuel&sc&rsrceca3hrspsh:5wngu o  sfdhehro  ecela cbuean / .terettor/lc  noalacfAhtqhad&eieafm=ulsrp.toe:/i/Awe iCrC i/  seouo hserdrervneu/hcpltrmtsyTyo ydrnlltowotuileics&soaveu=arEttE/s/ w wdTeTFt oye g.fhpai ,iosve wsrto:lhhlpe-hsmho lku.il npegs_nt_serti&dtcePp/n/ w .oieFsFue fo ur  tolgt fcterM eetm/bea :caii tufd tpodh-srhecciao%msdperksRsmgpcwMlft   ?ls>fuosa htplnhifo  sSCrvp//owc /.nss(t i gernetm:yl&olocu2a=ea_uis8:iirhwoi h-e- l  e nemhipueeetiriaePT-es ruikh/caI spanvo o?rta/=iiuunar0tnogsen-7/snaa.rvt  v - -bnhe  tg:lnd 'crnn 4Fcr: inr.tvolscu:raudiqd/pc/&gnrdsdcsso&ec ga0/cecnyeehrheh l esasowth/ag esuutde3 os/hndentumyLog/ell tuo2shlehcse=eet=ts=eh/c.m/etno oe/tnthih ir fhp /refv lpe n0bni/tgh.epl siug/ lni ecN:iextle_tm=uleo0nt cAiorieuov lttttstcvda i:qp soelttrig)atnwtzaot:n ibrepjyetpsIp/nat=uspriudibr&athePrpicltnebipsptttaelnmc/uwr)rneyifni srg3pecr//hhsrssiu,r etDD/eretd=lucsyvotcrptsRrena u revs sp prsydeh/ane  tf oatn ei.csrkgC/ut-aetcs aio.=Aw-nnretae_e&eo=oi:tssonglib/fse:o:so:ee  t plac h tpncrehdbkh:0e/owbtc,)eot bspc1Rwlidu_ry&irf%kplo/p?hrbFcseulto/n/:f/fcaaadwibehii r.eoet ura/trwuw.po  dc ri lo0yweneeculin&o2&ols/swosoor ./o v/l// /u nlsontlntgsoocsdrtlt/l/esanwcsua  tt/lcem7Y.agd&aeinsfr0fpe=i:tp.orygclwpecic/acloympeayetth ngo,uipee lia.rt.o:r hbfonil /3#pr._is&sctomoouctn/__okBpooi.lrtntcla stolsb . p ulrm cn:ad somogehm/spty.uete l0Eanopneitliranrltrv/mecsetlmvcaffeftlpochso lpkwsssie/atg/r h...rara//ert cctia i2cciruc_nsutmtlmaiuewcnf/god/eocl1/tf tfpitiaewra:cunsl i,/nctcncgm_c m/ap/ohsenhb1Ykneblsc=duasiaroenw=_.pig,womeo0iitCf  n tl.n/r/haesogo cihtoeo/eHk a csumies t/ otgilutltett=ntin&twIhbrnr av sw1rmiT.tcga lta g/ol igonstnapmtm sathx(t:/ nc  tuhvp-liduur_islest_iw.noeona'''  

def encrypt_message(key, message):
    cipher_text = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            cipher_text[column] += message[currentIndex]
            currentIndex += key

    return "".join(cipher_text)

def decrypt_message(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plain_text = [''] * numOfColumns
    column = 0
    row = 0

    for ch in message:
        plain_text[column] += ch
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    
    return "".join(plain_text)

cipher_text = encrypt_message(6, "Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November\
1852) was an English mathematician and writer, chiefly known for her work on\
Charles Babbage's early mechanical general-purpose computer, the Analytical\
Engine. Her notes on the engine include what is recognised as the first\
algorithm intended to be carried out by a machine. As a result, she is often\
regarded as the first computer programmer.")
print(cipher_text)
'''
cipher_text = encrypt_message(18, "Oi, shrimp gang, whatcha doin'?")
plain_text = decrypt_message(18, "Ohia,t cshhar idmopi ng'a?ng, w")
print(f"Ciphertext is: {cipher_text}")
print(f"Plaintext is: {plain_text}")
'''