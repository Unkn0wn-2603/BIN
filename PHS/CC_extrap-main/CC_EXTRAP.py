import os
logo = '''

  \033[1;91m██████╗░\033[1;92m██████╗░\033[1;96m██╗\033[1;93m██╗░░░██╗\033[1;94m░█████╗░\033[1;95m████████╗\033[1;92m███████╗
  \033[1;91m██╔══██╗\033[1;92m██╔══██╗\033[1;96m██║\033[1;93m██║░░░██║\033[1;94m██╔══██╗\033[1;95m╚══██╔══╝\033[1;92m██╔════╝
  \033[1;91m██████╔╝\033[1;92m██████╔╝\033[1;96m██║\033[1;93m╚██╗░██╔╝\033[1;94m███████║\033[1;95m░░░██║░░░\033[1;92m█████╗░░
  \033[1;91m██╔═══╝░\033[1;92m██╔══██╗\033[1;96m██║\033[1;93m░╚████╔╝░\033[1;94m██╔══██║\033[1;95m░░░██║░░░\033[1;92m██╔══╝░░
  \033[1;91m██║░░░░░\033[1;92m██║░░██║\033[1;96m██║\033[1;93m░░╚██╔╝░░\033[1;94m██║░░██║\033[1;95m░░░██║░░░\033[1;92m███████╗
  \033[1;91m╚═╝░░░░░\033[1;92m╚═╝░░╚═╝\033[1;96m╚═╝\033[1;93m░░░╚═╝░░░\033[1;94m╚═╝░░╚═╝\033[1;95m░░░╚═╝░░░\033[1;92m╚══════╝
  \033[1;96m
                  ██████╗░██╗███╗░░██╗
                  ██╔══██╗██║████╗░██║
                  ██████╦╝██║██╔██╗██║
                  ██╔══██╗██║██║╚████║
                  ██████╦╝██║██║░╚███║
                  ╚═════╝░╚═╝╚═╝░░╚══╝
'''
os.system("clear")
print (logo)


e = str(input("\033[1;96mEnter first CC: "))
f = str(input("\033[1;96mEnter second CC: "))
print("\n\033[1;97mGenarating CC\n")
ee = list(e)
ff = list(f)

e1 = ee[0]
e2 = ee[1]
e3 = ee[2]
e4 = ee[3]
e5 = ee[4]
e6 = ee[5]
e7 = ee[6]
e9 = ee[8]
e11 = ee[10] 
f1 = ff[0]
f2 = ff[1]
f3 = ff[2]
f4 = ff[3]
f5 = ff[4]
f6 = ff[5]
f7 = ff[6]
f9 = ff[8]
f11 = ff[10]

ep = e1 + e2 + e3 + e4 + e5 + e6 + e7 + 'x' + e9 + 'y' + e11 + 'z' + '2441'
fp = f1 + f2 + f3 + f4 + f5 + f6 + f7 + 'x' + f9 + 'y' + f11 + 'z' + '2441'



p = -1
while p<=998:
    p = p + 1
    v = str(p)
    b = (str(v).zfill(3))
    #print(nirob)
    bb = list(b)
    x = bb[0]
    y = bb[1]
    z = bb[2]    
    epp = str(ep).replace('x', x).replace('y', y).replace('z', z)
    fpp = str(fp).replace('x', x).replace('y', y).replace('z', z)
    
    eee = list(epp)
    fff = list(fpp)
    ee1 = epp[0]
    ee2 = epp[1]
    ee3 = epp[2]
    ee4 = epp[3]
    ee5 = epp[4]
    ee6 = epp[5]
    ee7 = epp[6]
    ee8 = epp[7]
    ee10 = epp[9]
    ee11 = epp[10]
    ff1 = fpp[0]
    ff2 = fpp[1]
    ff3 = fpp[2]
    ff4 = fpp[3]
    ff5 = fpp[4]
    ff6 = fpp[5]
    ff7 = fpp[6]
    ff8 = fpp[7]
    ff10 = fpp[9]
    ff11 = fpp[10]
    
    k = int(ee10) + int(ee11) 
    kl = k//2
    kll = kl * 5
    
    j = int(ff10) + int(ff11)
    jl = j//2
    jll = jl * 5
    
    ult = kll + jll
    res = str(ult)
    
    cc1 = ee1 + ee2 + ee3 + ee4 + ee5 + ee6 + ee7 + ee8 + res + 'xxxxxx'
    cc2 = ff1 + ff2 + ff3 + ff4 + ff5 + ff6 + ff7 + ff8 + res + 'xxxxxx'    
    print(cc1)
    print(cc2)
print("\n\033[1;95mCC generated sucessfully!! Created by \033[1;91mR00tdev1l of PHSquad\033[1;95m & Customize by \033[1;96mErrorXploit\n")    
    
    
    
    
    
    
    



