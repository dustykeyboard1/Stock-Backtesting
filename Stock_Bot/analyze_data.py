import pickle 
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt






test_list = ['AMX', 'NAC', 'PLCE', 'CO', 'FCF', 'AMPG', 'GIL', 'EOI', 'ATCO', 'SKM', 'SONO', 'AB', 'BSAC', 'WIT', 'FRME', 'PIO', 'ZH', 'PPL', 'CAG', 'OXLCM', 'UPST', 'ALLG', 'WISH', 'CNTX', 'HZO', 'DRCT', 'MORF', 'IIIN', 'LYLT', 'MBWM', 'SYF', 'EPSN', 'STGW', 'CEM', 'BSIG', 'IMXI', 'FYBR', 'CRWS', 'NCR', 'OCGN', 'GHM', 'JNPR', 'MARA', 'MVST', 'FTCH', 'ADV', 'CATY', 'AX', 'NEPT', 'GOGL', 'CMCO', 'ZTO', 'AGIO', 'MXCT', 'NRDS', 'CERT', 'AGS', 'CAL', 'KOS', 'GILT', 'LBTYA', 'PARAA', 'AMPS', 'BBDC', 'WSBC', 'POWW', 'AEL', 'VIVK', 'CYN', 'XOS', 'KBAL', 'ONB', 'JAKK', 'PUBM', 'CHX', 'XRX', 'RFM', 'CREX', 'IPG', 'HRTX', 'ALLK', 'SWIM', 'STRC', 'FNCH', 'SLF', 'FFIE', 'ELY', 'IMGN', 'VFF', 'AUGX', 'CCCS', 'AKR', 'AAL', 'CRMD', 'SSRM', 'IBN', 'IDYA', 'MCS', 'NGM', 'WFC', 'CVE', 'FTI', 'SKYX', 'BSCM', 'ORI', 'XENE', 'ATHE', 'LAUR', 'ARCC', 'BBAR', 'JNCE', 'PCQ', 'VGR', 'MRC', 'SCKT', 'BTU', 'CYH', 'LGF.B', 'ACCD', 'OPFI', 'DRVN', 'VORB', 'UPWK', 'ORAN', 'MRTN', 'SGHT', 'INTA', 'NDLS', 'SOND', 'FOX', 'CHRA', 'BSCR', 'PIE', 'RMMZ', 'DHC', 'NVTA', 'MITO', 'GDEN', 'CHWY', 'BLND', 'HLF', 'PAYO', 'VIV', 'MDC', 'JMIA', 'LIDR', 'QSI', 'EAR', 'DELL', 'NUVB', 'CMPO', 'FMNB', 'NMIH', 'MDIA', 'MKTW', 'SY', 'HWM', 'CARS', 'PRFX', 'LTRPA', 'MCRB', 'APAM', 'NKLA', 'IMTE', 'UIS', 'PRTA', 'XPEV', 'SG', 'AMSC', 'HTBK', 'DADA', 'RPAY', 'GDS', 'XM', 'CARR', 'TMHC', 'NYMT', 'TWKS', 'TWOU', 'MAXN', 'UAL', 'IMUX', 'MATV', 'COOK', 'RBBN', 'NWSA', 'ETON', 'DLX', 'HIMX', 'CNTB', 'GATO', 'MESA', 'PNTG', 'CAKE', 'ABEO', 'BCYC', 'BLI', 'REYN', 'GDYN', 'SMFL', 'NBXG', 'OUST', 'ALSN', 'BIOR', 'ANGI', 'S', 'CHGG', 'SBGI', 'PZC', 'SDIG', 'TXG', 'ANF', 'VZ', 'IRWD', 'VRAY', 'NRGV', 'SAVA', 'SHIP', 'CTBB', 'CWBR', 'BSCQ', 'BFLY', 'PEGA', 'LNSR', 'LMDX', 'VTEX', 'ML', 'FUV', 'CDLX', 'SWVL', 'IMAB', 'FREE', 'CUBI', 'DERM', 'SWI', 'ERIC', 'ALVR', 'EVTC', 'BILI', 'ACT', 'AUY', 'ONTF', 'CFVI', 'NTST', 'KALV', 'OPRX', 'STRN', 'BBLN', 'VERB', 'BRMK', 'MDVL', 'VTRS', 'FSR', 'ATXI', 'FGF', 'NBTB', 'ONEM', 'X', 'EAI', 'WORX', 'CGEM', 'BKKT', 'RRR', 'BSCP', 'FULC', 'XERS', 'BTCY', 'FPXI', 'GRAB', 'AADI', 'MOMO', 'NNY', 'EVF', 'ABR', 'GAME', 'PTVE', 'BIPH', 'CARG', 'DNMR', 'ZWS', 'OCUL', 'LOVE', 'VRNT', 'SGMO', 'TBLT', 'WB', 'PAVM', 'RNW', 'GBX', 'LSXMK', 'SCSC', 'EQRX', 'SGHC', 'GLUE', 'ASTE', 'CVGI', 'RLAY', 'VAXX', 'NKTR', 'ATLCL', 'NEOG', 'OSBC', 'HGV', 'BDN', 'KVHI', 'ZG', 'EC', 'DX', 'VNDA', 'CERE', 'CDE', 'OSPN', 'COOP', 'TGI', 'OLP', 'TRS', 'ARHS', 'FAMI', 'WPM', 'LABP', 'SWBI', 'LUCD', 'PHM', 'VERI', 'PGZ', 'LOB', 'UFCS', 'CCRN', 'ESTE', 'STNE', 'FATE', 'NU', 'VERV', 'USER', 'ICPT', 'SEAC', 'OPK', 'UBS', 'MCG', 'STG', 'BCOR', 'FFIN', 'TDCX', 'JANX', 'GLAD', 'LDP', 'SGBX', 'RILYT', 'GGR', 'KNSA', 'FPAY', 'PSHG', 'ATRO', 'AMKR', 'MLCO', 'GHL', 'INSE', 'ATER', 'LOCL', 'BSL', 'SIX', 'RERE', 'WOOF', 'VERA', 'HLLY', 'ISEE', 'CGEN', 'KN', 'BPYPN', 'EFSC', 'SQSP', 'TVTX', 'PFLT', 'WY', 'BAND', 'CND', 'BCML', 'HYPR', 'GMTX', 'FANH', 'NWS', 'EFTR', 'REFI', 'AQB', 'KRG', 'MTRX', 'BFH', 'EGLX', 'CRH', 'JYNT', 'HLTH', 'PANL', 'VIRT', 'THR', 'HIX', 'SPWH', 'CLAR', 'MUX', 'ATI', 'BBQ', 'MDXG', 'ELAN', 'NVOS', 'ARQQ', 'LDI', 'ATHX', 'SLNO', 'ARI', 'KDP', 'ANGO', 'HCP', 'IRS', 'KTB', 'ECVT', 'BKE', 'EDTK', 'MDRR', 'STON', 'LSEA', 'AVNW', 'NXC', 'FBC', 'BSCN', 'INO', 'SEAT', 'PFHD', 'XFOR', 'DMB', 'LTCH', 'LBAI', 'QUOT', 'ALIT', 'THFF', 'UE', 'VTYX', 'WSBF', 'PLAY', 'MAXR', 'TRQ', 'IMV', 'AUDC', 'WINT', 'INVZ', 'AGNC', 'ACB', 'CHUY', 'BTO', 'ALLY', 'CG', 'OM', 'KT', 'BNY', 'RTL', 'CIDM', 'IHRT', 'IEA', 'IGR', 'KAMN', 'KERN', 'T', 'ADCT', 'KLTR', 'ACH', 'SBS', 'THRY', 'IBTE', 'RYN', 'DWAC', 'ANAB', 'TIL', 'GPRO', 'MDRX', 'GGAL', 'TGH', 'CTKB', 'TIG', 'BFIN', 'CXSE', 'ISPO', 'VRM', 'UTRS', 'SFNC', 'ADNT', 'AVXL', 'SLQT', 'RETA', 'SMPL', 'NLY', 'VNO', 'COLB', 'HASI', 'OGE', 'GGB', 'CYCC', 'BRFS', 'AEHR', 'SHI', 'DDD', 'CWCO', 'GM', 'PRTY', 'LVOX', 'HLBZ', 'LWLG', 'FL', 'SUNW', 'AMH', 'VTIP', 'CHY', 'NOAH', 'LUNA', 'RUBY', 'INM', 'PAGP', 'AVTR', 'LTRY', 'ROL', 'FOXA', 'HLMN', 'MGM', 'KREF', 'PFH', 'EEX', 'CTRA', 'CEAD', 'LI', 'DM', 'BSGM', 'ASUR', 'KD', 'MAC', 'DRD', 'CBAY', 'FRGT', 'BRX', 'TSP', 'AAT', 'ENR', 'JRVR', 'TPC', 'TFSL', 'PSTV', 'CLBS', 'AOUT', 'PHUN', 'ACVA', 'PSNL', 'DSKE', 'UPLD', 'KNTE', 'POAI', 'SHOP', 'DNLI', 'IRNT', 'CELC', 'CRIS', 'TPH', 'CXM', 'ICL', 'IS', 'SKIL', 'SHBI', 'AVNT', 'GOEV', 'MIRO', 'TLYS', 'ARCT', 'MAIN', 'BK', 'E', 'TDS', 'DENN', 'XMTR', 'AGL', 'CTOS', 'VSEC', 'SDVY', 'RIGL', 'JBGS', 'OSUR', 'VTNR', 'CSTM', 'GO', 'TPX', 'BAOS', 'PDD', 'ALZN', 'CABA', 'TTOO', 'TMDI', 'SQQQ', 'BHFAO', 'RXT', 'PRIM', 'DZSI', 'AMBC', 'DICE', 'CHRS', 'KMT', 'SUSB', 'TH', 'KPRX', 'WAFD', 'AM', 'SECO', 'AVDL', 'CPNG', 'LILM', 'XIN', 'HAYW', 'INDI', 'TLIS', 'CNSP', 'LILAK', 'TNL', 'OP', 'CURV', 'VBIV', 'HPP', 'AMRK', 'EGY', 'BVH', 'DCT', 'ASB', 'RITM', 'RVNC', 'VZIO', 'VRDN', 'FBRX', 'LSXMA', 'ETRN', 'NVAX', 'PNM', 'ILPT', 'EBAY', 'YETI', 'FPI', 'MMU', 'VIPS', 'AMPH', 'CMTG', 'AES', 'NETI', 'WNC', 'AEVA', 'ENDP', 'STM', 'CVT', 'ZIP', 'EDAP', 'POLA', 'PRG', 'BTB', 'BEKE', 'GAB', 'EQNR', 'CSX', 'LPTX', 'DNAY', 'BHE', 'EBS', 'ESRT', 'BOLT', 'SONX', 'BBWI', 'COLL', 'FMTX', 'GLMD', 'PUMP', 'INBK', 'KRMD', 'FCX', 'CYRX', 'MDV', 'SNY', 'MNTV', 'VLRS', 'LFG', 'NN', 'CSII', 'HURC', 'DT', 'BLCN', 'INMD', 'ASZ', 'ONL', 'WERN', 'VSTO', 'CASH', 'CENN', 'EXEL', 'BALY', 'RSI', 'TLRY', 'ESMT', 'HA', 'NLS', 'REKR', 'ORGO', 'AIRC', 'MGI', 'ORC', 'FORR', 'WSC', 'VSCO', 'ESNT', 'LZB', 'FORM', 'OPRT', 'WEN', 'IMBI', 'SRRK', 'FSK', 'DESP', 'CNSL', 'CLMT', 'FOUR', 'JXN', 'GUG', 'ODP', 'APYX', 'AERI', 'PRA', 'TNGX', 'BIG', 'BOX', 'KLR', 'NAUT', 'HEPA', 'IAS', 'BRSP', 'CX', 'RWT', 'SFIX', 'BOXD', 'GNW', 'ARR', 'SVFAU', 'CEQP', 'AR', 'HSBC', 'LQDA', 'CMC', 'LCID', 'GREEL', 'CGNT', 'KRNY', 'AMRX', 'TPB', 'MFG', 'TQQQ', 'SHCR', 'NWG', 'BCS', 'CMPR', 'MTR', 'ORIC', 'AUB', 'SRC', 'AUD', 'SGML', 'MF', 'AUPH', 'OMF', 'MAT', 'IPOF', 'YEXT', 'CFRX', 'QNGY', 'GSM', 'BCAB', 'TALK', 'UMPQ', 'VWE', 'RYAM', 'LGF.A', 'ONDS', 'EXAS', 'HEXO', 'RGTI', 'INSM', 'ALTG', 'FIXD', 'TFFP', 'QGEN', 'CDXS', 'ABVC', 'SKYW', 'MBI', 'SBOW', 'SWN', 'BHFAP', 'NXPL', 'VREX', 'EVTL', 'XELB', 'CRC', 'TPST', 'PWP', 'CAN', 'LTC', 'ITI', 'EGRX', 'RKT', 'TEI', 'PLTK', 'CNNE', 'PAY', 'SPCB', 'FISI', 'PCH', 'NRDY', 'MO', 'RCA', 'BZUN', 'PACB', 'ARCO', 'EAT', 'AGEN', 'SUM', 'NSPR', 'MKD', 'NVVE', 'CRD.B', 'EXPI', 'ATY', 'DXC', 'OCCI', 'WEAV', 'TGNA', 'BUSE', 'IQI', 'RSSS', 'NRG', 'ABCM', 'FLGC', 'YY', 'SANM', 'RNP', 'MGTX', 'NGL', 'AXSM', 'TBB', 'GENI', 'AROC', 'MNDT', 'RADI', 'FGEN', 'TK', 'SVFD', 'EXAI', 'AKA', 'SLDP', 'NGMS', 'NOK', 'GROM', 'IMRA', 'AZUL', 'BHLB', 'ALGM', 'PTRA', 'ROCK', 'KBNT', 'AMBP', 'DAVE', 'SPRO', 'ATGE', 'GPS', 'AEO', 'CFFN', 'BHG', 'TGLS', 'AY', 'SPCE', 'CLB', 'LMND', 'DCOM', 'EMF', 'CASS', 'PAYA', 'MINM', 'MSGM', 'LU', 'UMC', 'NE', 'PACK', 'COWN', 'WIZ', 'SASR', 'TUR', 'OGI', 'EVBG', 'NTCT', 'NEO', 'PETS', 'LIFE', 'GFI', 'DGICA', 'CSCO', 'LESL', 'NAT', 'MEKA', 'ACNT', 'INBX', 'SNAP', 'GCI', 'LGMK', 'HCSG', 'UCBI', 'AXTI', 'ROIC', 'KIM', 'CSSE', 'KTOS', 'AIQ', 'QTEK', 'HTZ', 'JAMF', 'PBPB', 'UP', 'SIGA', 'BSY', 'SBTX', 'PTE', 'HTHT', 'CMP', 'BHIL', 'STER', 'ONCT', 'ST', 'RDWR', 'LLL', 'HFWA', 'EPRT', 'ARLO', 'TERN', 'GOLD', 'NRIM', 'SAN', 'DS', 'BSBR', 'EGO', 'SZC', 'INFA', 'EYPT', 'HIPO', 'YPF', 'SIGIP', 'IIM', 'SPR', 'ME', 'BRLT', 'RMNI', 'SEMR', 'BOOM', 'NIO', 'HEES', 'AMRS', 'GOGO', 'ACAD', 'PBR', 'ONON', 'ORCC', 'NNN', 'DOUG', 'WBND', 'FINV', 'EXFY', 'EGIO', 'LEGN', 'IPSC', 'PEAK', 'AMRN', 'PTGX', 'CELU', 'CARA', 'KNDI', 'QUAD', 'EXC', 'FORG', 'NVEI', 'GLDI', 'MRVI', 'APEN', 'DCP', 'SQZ', 'LSAK', 'BXSL', 'PRMW', 'FVRR', 'TPVG', 'BBGI', 'VLN', 'PGEN', 'HLGN', 'KSS', 'PMD', 'PRGO', 'TEF', 'BEN', 'SCPL', 'STOK', 'INCR', 'FBMS', 'FBP', 'ETD', 'KTTA', 'KR', 'WRE', 'SSKN', 'GTES', 'M', 'ENFN', 'HAIN', 'TIGO', 'SPNT', 'EDR', 'LAW', 'IBTK', 'SHC', 'TCRX', 'DMS', 'FIBK', 'PLTR', 'AZEK', 'CINC', 'HMC', 'VLY', 'OWL', 'ASRV', 'INOD', 'IVT', 'HBM', 'OUT', 'HONE', 'SPFI', 'BKEPP', 'GTX', 'OMIC', 'CNF', 'ENVA', 'GF', 'NPV', 'ARMK', 'ANPC', 'MP', 'MGNX', 'OI', 'VMBS', 'VIAV', 'RUTH', 'SCHL', 'CMCT', 'B', 'ALEX', 'SBSI', 'IFRX', 'ARAV', 'CTIC', 'GRWG', 'INSG', 'NEM', 'GRPH', 'EQH', 'DHCNL', 'WBX', 'HBI', 'HTLF', 'HTD', 'CYXT', 'STEP', 'FDMT', 'AVIR', 'TDOC', 'HBNC', 'PGTI', 'ZCMD', 'JPT', 'GIII', 'CXW', 'CRTO', 'OMGA', 'IBOC', 'KPTI', 'ABB', 'VSAT', 'EDIT', 'SIOX', 'GMRE', 'TMCI', 'HR', 'NCTY', 'DYAI', 'ECOM', 'SLGC', 'ADTN', 'XRAY', 'TIGR', 'BIOC', 'AMTD', 'NYCB', 'AVCT', 'HOOK', 'BTAI']
#print(len(list) / 50)
newlist = list(set(test_list))
print(len(newlist))

#plt.title(line2)

#plt.show()