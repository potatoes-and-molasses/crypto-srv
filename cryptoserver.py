import socket
import subprocess
import thread
import os
import re
import string
import random
import subprocess
import time
from Crypto.Cipher import AES
############################################################################
##############DONT READ THIS IF YOU DONT WANT SPOILERS######################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################

def parsedata(st):
    match = re.search('^yoozerneym=(.*?)&paswrd=(.*?)&morestuff=(.*)&admin=(\d)',st)
    if match:
        return tuple([i.replace('&','') for i in match.groups()])
    return tuple([None]*4)
def binlol(char):
    return ('%8s' % bin(ord(char))[2:]).replace(' ','0')
auth = {('useruser','p@ssw0rd'):1,
        ('maybekindasorta','whatRtheseOfulW0rds'):2,
        ('good_usernam3','lolno!blah'):3,
        ('tempname','T3MpPa55wOrd='):4,
        ('guesstimate','2b||!2b'):5,
        ('mspa','abscond!'):6,
        ('nope','R3tr1ev3@rmsFr0mSafe'):7,
        ('copypasta','blockcipherthings'):8,
        ('someperson','descriptivePhrase'):9,
        ('inprogress','orsomething'):10,
        ('tobecontinued','soon!'):11}
auth2 = {i:j for j,i in auth.iteritems()}

flags = {1:'this temporary text will be replaced with enticing and witty commentary about life!',
         2:'This building flies through space just above the air. People from different countries built it and fly up to visit it in space boats. Because the house is falling around the Earth, things inside it hang in the air instead of dropping to the floor. Inside the house, normal things like water act very strange, and you can fly around by kicking off the walls. Everyone says it is a lot of fun. The people in the house spend their time working, playing, and taking pictures of Earth. They do work for people on the ground, helping to learn how things like flowers and machines work in space. Most of the time, there are six people in the house, with each person staying for half a year. A big reason we built the space house was so we could learn to keep people alive and strong in space for months or years without getting sick. We will need to be good at that if we ever want to travel to other worlds. To build the space house, we took each piece up in a boat, pushed it until it went really fast, then caught up to the house, and stuck the part to the house.',
         3:'normal sky boats have to go fast so the air hits their wings hard enough to hold them up if they fly too slow they fall sometimes falling makes them go fast enough to fix it this boat works just like those sky boats but it uses a cool idea instead of the whole boat going fast only its wings go fast the rest of the boat can go as slowly as it wants or even stop and sit in one place in the sky if a normal sky boat had wings that went faster than its body the wings would fly away but this boats wings go in a circle that keeps them near enough to hold on to while still going around fast enough to fly',
         4:'before we start hi we are the people in these little countries called states and we want to get together into a country we want to make everything nice and quiet keep anyone from hurting us and make sure our kids will be free thats why we are making a country here are its laws book one the law makers part one laws are made by a group called law makers there are two rooms of law makers the house and the serious room part two the people pick law makers to send to the house for two years at a time bigger states get to have more people in the house oh and the country needs to count its people sometimes so it can figure out how many chairs the room needs part three every state sends two law makers to the serious room for six years at a time they cant be too young part four states make the laws about where and how people get together to pick leaders and decide what the country should do part five when the law makers get together they should write down what they talk about part six law makers get paid they cant get in trouble for what they say at work but they also cant do any other job for the country while theyre law makers part seven if the law makers have an idea for a new law and more than half the people in both rooms say they like it they send the idea to the countrys leader to be made into a law if the leader doesnt like the idea the law makers can still make it a law but it takes more of them part eight law makers are allowed to take money from people but only sometimes and they cant just take it all from one person or anything like that they are allowed to use the money to build certain kinds of things like letter boxes and boats with guns on them they can get people in trouble for a few things like stealing boats even if they do it far away or making pretend money and telling people its real part after eight there are lots of things the law makers arent allowed to do they cant make up laws to lock someone up for something they already did or give some people special names that mean theyare more important to the country than others part ten there are some things the country can do that the states cant like creating money or starting wars the states also cant take money from other states or put guns on boats book two the leaders part one every four years the people in the country pick who should lead them they pick a first leader who is the head of the country and a second leader who isnt if the first leader leaves or gets fired the second leader takes over the work the first leader was doing the states get to choose the leaders by a point system where each state gets one point for each law maker it has part two the leader controls the people who fight for the country the leader can also can talk to the leaders of other countries and get anyone out of trouble part three now and then the first leader should let the law makers know how everything is going and suggest some ideas part four the law makers can fire the first leader but only for doing something really bad like becoming leader of another country at the same time and having them attack us or stealing the countrys money and going to live on a boat book three the law deciders part one theres a group of people called the top law deciders they help decide whether laws have been broken the country can set up other groups of law deciders too but theyre not as important as the top law deciders part two the top law deciders only decide certain kinds of law fights like if the leaders of another country send someone here and they get in a fight or when someone has a law fight with a state the rest of the time they can only step into certain law fights and only when another decider has decided something and the people in the law fight dont agree part three turning against the country can only mean a few very clear things fighting us joining a group thats fighting us or helping a group thats fighting us to prove someone has turned against the country two people need to say they saw it or the person has to have admitted it in a deciding room law makers can make turning against the country against the law but they cant use it as a reason to do whatever they want to someone this had been a problem in some other countries book four the states part one there are states and they have to get along when the law deciders in one state decide something the law deciders in other states dont have to make that choice the same way but they cant make it so the other choice doesnt count that means that if someone gets in trouble in a state they cant go to another state and get a law decider to tell them they are not really in trouble after all part two you have the same rights no matter what state youre from also if you get in trouble in one state and run away to another the other state has to send you back to the first one part three the country can add new states the country can also own areas of land inside states to be used for things the country needs just like people do part four the country promises that every state will be run by its people and that if someone attacks or if they have a problem and ask for help the whole country will come and fight for them book five making changes people can change these laws but most of the law makers and most of the states have to agree on the change it cant just be a little more than half it has to be most of them if the states want to make a change without the law makers the states can also hold a big law party where each state comes and shares their ideas for changes and then they decide which ones they like book six everyone listen up these laws are important and everyone has to follow them also if the country agrees on something with another country thats important too other laws are important but less so anyone working for the country has to promise that they are on our side but they never have to say anything about god book seven does this all count yet this country only becomes real if more than eight states join ten changes change one the country cant make laws about god it also cant make laws about what people talk about who they hang out with or what they write about and cant stop them from telling the leaders if they are angry about something as long as theyre not starting fights change two since having welltrained normal people with guns is important for keeping the country safe no stopping people from having guns change three just because someones fighting for the country doesnt mean you have to let them stay in your house change four the police cant go through your stuff without a good reason and a special pass from a law decider change five the police cant do stuff to you just because they want to they need to make it clear what you did wrong they can never make you admit you broke a law change six if you get in trouble you can have a chance to fight about it in front of a group of normal people in a deciding room and you can always have someone who knows about laws to help you if you want if someone says you did something bad you get to talk to them face to face change seven you can have your law fight in front of a group of normal people even if you are not in trouble change eight police cant be mean for fun even to bad people change after eight people can do stuff not talked about here change ten the country can only do the things these laws let it do the states can do whatever more changes change people cant have law fights with other statesonly their own change we changed the laws for how we pick leaders change we just had a big war with some states over whether its okay to buy humans and force them to work the side that said no won no more buying humans or forcing them to work change also now that the war is over we are adding a number of laws about what states can and cant do to people change oh and people of any skin color can help pick leaders and decide what the country will do change the country can take some of your pay to get money for things we need change people not a states leaders pick the law makers who will sit in the serious room change lets get rid of beer and wine change people of any sex can help pick leaders and decide what the country will do change we moved up some of the days when new leaders take over for the old ones because we have cars now and dont need to allow a few months for people to travel change never mind about getting rid of beer and wine change you cant be the first leader forever change people in the special town where the leaders and law makers live can help pick leaders and decide what the country will do just like if they lived in a normal state change no making people pay to help decide things change we made it clearer what happens when a leader dies or leaves change younger people can help pick leaders now change if law makers decide to change how much they are paid they dont get the new pay until after the people in their state have had a chance to decide whether to fire them and pick someone else',
         #5:'no_flag_in_this_stage_for_now_loool',
         6:'cats_ArE_qUite_Okay',
         7:'@ll_Th3_luck.all-of-it',
         #8:'noflaglol@doesntmatter',
         #9:'neither',
         10:'iM_r3aD1ng-theW@ll,theyRwallW0rds'}

msgs = {1:'this was easy:)\r\n(next stage credentials below)',
        2:'xoring the stuff for fun & profit!',
        3:'nicely done//whatnow',
        4:'yup, that\'s it. next on, AES',
        5:'just so! and now can you decrypt ecb?\r\nin the next stage the flag is appended to your data before encryption',
        6:'indeed^^ and next, the same thing with some more random nonsense before your data as well!',
        7:'and now... move some blocks around!',
        8:'time for cbc:) flip some bits & get an admin token. special character filtering might be applied to your input',
        9:'not bad! next one is a CBC padding oracle, PKCS7 padding is in use.',
        10:'you win, for now... congrats:D'}
for i in msgs:
    msgs[i]+='\r\n{'+'{}:{}'.format(auth2[i+1][0],auth2[i+1][1]) + '}'
BONUS_FLAG='{Oh_s0_U-Man@g3d=2readThis?:amazing!}' #only obtainable through pickle shenanigans, I hope:D
BONUS_PASSWORD='this authentication process is astoundingly bad, i see no reason to use it over some nice uncommon password such as qwertyuiop[]'
PICKLEJAR_ASCIIART=open('jar.ascii','r').read()
CANNED_FOODS = ['canned can','canned canoe','canned canyon', 'canned cannon', 'canned canine','canned canary', 'canned bad joke that assumes the usage of words that sound like "can" can amuse people in this context','pickles']
NO_BEEP = [i for i in range(256) if i!=7]
class session:

    def __init__(self,conn):
        self.conn = conn
        self.ecbguess_score = 0
        self.stage6ecbenc = AES.new(rkey(16),AES.MODE_ECB)
        self.stage7ecbenc = AES.new(rkey(16),AES.MODE_ECB)
        self.stage8ecbenc = AES.new(rkey(16),AES.MODE_ECB)
        self.stage9cbckey = rkey(16)
        self.stage9cbciv = rkey(16)
        self.stage10key = rkey(16)
        self.stage10iv = rkey(16)
        self.bonusid = str(random.randint(1000000,10000000))

    def init_folders(self):
        if self.bonusid in os.listdir(r'anon'):
            return
        os.mkdir(r'anon\{}'.format(self.bonusid))
        with open(r'anon\{}\cmds.conf'.format(self.bonusid),'wb') as f:
            f.write('dir anon\\{}\n'.format(self.bonusid))
            f.write('echo hurray!\n')
            f.write("python -c \"import pickle;pickle.load(open(r'anon\\{}\\jar','rb'))\n".format(self.bonusid))
            f.write("python -c \"import pickle;pickle.load(open(r'anon\\{}\\jarjar','rb'))\n".format(self.bonusid))
            f.write('type anon\\{}\\cmds.conf\n'.format(self.bonusid))
            f.write('type anon\\{}\\jar\n'.format(self.bonusid))
            f.write('time /t')
        with open(r'anon\{}\jar'.format(self.bonusid),'wb') as f:
            f.write("(S'how rude!'\np0\nS'he always succeeds to succeed'\np1\ntp2\n.")
        with open(r'anon\{}\jarjar'.format(self.bonusid),'wb') as f:
            f.write("cos\nsystem\n(S'cmd.exe /c dir C:\users\'\ntR.")
        time.sleep(1)
            
            
            
            
    def dostuff(self,connectiondata):
        user,password,data,admin = parsedata(connectiondata)
        #print user,password,data,admin
        if admin=='1':
            return 'cleartext admin authentication disabled'
        if admin=='2':
            return 'nah, still disabled:D'
        if admin=='3':
            return "try a bit harder, maybe you'll get a shell"
        if admin=='4':
            return 'PS C:\\users\\administrator>'
        if admin=='5':
            return 'nah just kidding'
        if admin=='6':
            return 'why even bother with this nonsense, focus on the fun crypto challenges instead!'
        if admin=='7':
            return 'nooo, go away! nothing to see, nothing to hear.'
        if admin=='8':
            return 'fine, fine, this is the bonus stage! it is pretty hard though so you might want to try other stuff first'
        if admin=='9':
            self.init_folders()
            res = (self.sndrcv('...sessionid:{}...\r\nplease choose an authentication type: \r\n1 - challenge-response \r\n2 - pass \r\n3 - anonymous'.format(self.bonusid))).lower()
            if res in ['3','anonymous']: #limited shell
                cmds = open(r'anon\{}\cmds.conf'.format(self.bonusid),'r').read().replace('\r\n','\n').split('\n') #will have some random useless cmds, dir .\anon and python -c "import pickle;pickle.loads(...."
                res = self.sndrcv('anon-shell>')
                while res in cmds:
                    res = self.sndrcv(subprocess.check_output(res,shell=1)+'\r\nanon-shell>')
                
                return 'only allowed to execute commands explicitly allowed in anon\\{}\\cmds.conf!\r\nterminating session...'.format(self.bonusid)
            elif res in ['2','pass']: #create pickle file
                res = self.sndrcv('enter password:')
                print [res]
                if res == BONUS_PASSWORD[-12:]:
                    res = self.sndrcv('approved.\r\nwelcome to can town v4.13, the best canned foods facility on this server(and probably in the whole universe).\r\n{}\r\nwhat kind of canned delicacy would you like to make?\r\n{}\r\n'.format(PICKLEJAR_ASCIIART,'\r\n'.join(CANNED_FOODS))).lower()
                    if res not in CANNED_FOODS:
                        return 'how uncanny, {} is not availble at the moment'.format(res)
                    else:
                        if res=='pickles':
                            res = self.sndrcv('whats in the jar?')
                            with open(r'anon\{}\jar'.format(self.bonusid),'wb') as fff:
                                fff.write(res)
                            return 'sending 1x{} by user request...\r\n{}'.format('pickles',PICKLEJAR_ASCIIART)
                        else:
                            return 'sending 1x{} by user request...\r\n{}'.format(res,PICKLEJAR_ASCIIART)
                else:
                    return 'this is indeed a password, well done! but unfortunately it is not the correct one for this stage:('
                    
            elif res in ['1','challenge-response']:#obtain password for 2.
                res = self.sndrcv('authentication scheme: 1024 blocks of data(16 bytes each) will be sent one after the other, each of them needs to be encrypted[AES_ECB,key = md5(PASS_FOR_STAGE_X+N*"lol"), where N is the block_number and X is 1+block_number%10] and sent back to the server for validation. all 1024 blocks need to be validated before login is permitted.\r\nproceed?(y/n)').lower()
                if res=='n':
                    return 'kthxbye'
                if res=='y':
                    passbits = ''.join(binlol(hehe) for hehe in BONUS_PASSWORD)#beeps as 1s and no beeps as 0s, result is BONUS_PASSWORD which lets you connect to the pickle interface and make pickles
                    for i in passbits:
                        block = rkey(16)
                        repl = random.choice(NO_BEEP)
                        if i=='1':
                            c_beeps = block.count('\x07')
                            if c_beeps==0:
                                to_change = random.choice(block)
                                block = block.replace(to_change,'\x07',1)
                            elif c_beeps>1:
                                block = block.replace('\x07',chr(repl),c_beeps-1)
                        else:
                            
                            block = block.replace('\x07',chr(repl))
                        self.sndrcv(block)
                    return 'validation failed. access denied. or maybe i just did not feel like letting you in. who knows?'
                            
                else:
                    return 'good elephant'
                    
        if (user,password) in auth:
            stage = auth[(user,password)]
        else:
            return 'omg no dis iz not cool maybe use some proper creds'
        #if data == flags[stage]:
        #    return msgs[stage]+'|'+'#'.join(auth2[stage+1]) 
        if stage == 1: #singlexor
            challenge = flags[stage]
            key = rkey(1)
            res = self.sndrcv(xor(challenge,key))
            if res == challenge:
                return msgs[stage]
        elif stage == 2: #multixor
            challenge = flags[stage]
            key = rkey(random.randint(4,8))
            res = self.sndrcv(xor(challenge,key))
            if res == challenge:
                return msgs[stage]
        elif stage == 3: #caesar
            challenge = flags[stage]
            key = random.randint(1,25)
            res = self.sndrcv(caesar(challenge,key))
            if res == challenge:
                return msgs[stage]
        elif stage == 4: #vignere
            challenge = flags[stage]
            key = ''.join([random.choice(string.ascii_lowercase) for i in range(random.randint(5,7))])
            res = self.sndrcv(enc4(challenge,key))
            if res == challenge:
                return msgs[stage]
        elif stage == 5: #ecb detection(50% ecb 50% cbc)
            if data=='':
                return 'give me some data to encrypt!'
            isecb = random.randint(0,1)
            key = rkey(16)
            if isecb:
                enc = AES.new(key,AES.MODE_ECB)     
            else:
                enc = AES.new(key,AES.MODE_CBC,'\x00'*16)
            res = enc.encrypt(pad0(data,16))
            tmp = self.sndrcv('[{}]\r\nis that encrypted in ecb mode?(y/n)'.format(res))
            ans = 1 if tmp=='y' else 0 if tmp=='n' else -1
            if ans == isecb:
                self.ecbguess_score += 1
                guess_quota = 100
                if self.ecbguess_score == guess_quota: #make this something big so this has to be automated
                    res = msgs[stage]
                else:
                    res = 'nice guess, {}/{}'.format(self.ecbguess_score,guess_quota)
            else:
                self.ecbguess_score = 0
                res = 'bad at guessing??'
            
            return res
        elif stage == 6: #ecb byte at a time to obtain suffix
            challenge = flags[stage]
            res = self.sndrcv(self.stage6ecbenc.encrypt(pkcs7(data+'<IMPORTANTSTUFF lolol/>btwtheflagis:{}'.format(challenge),16)))
            if res == challenge:
                return msgs[stage]
        elif stage == 7: #6 with random length data as prefix
            challenge = flags[stage]
            lolwut = pkcs7('<nicest_metadata_ive_seen_{}'.format(rkey(random.randint(5,15)))+data+'<IMPORTANTSTUFF lolol/>[and]thisflagis:{}'.format(challenge),16)
            print lolwut
            res = self.sndrcv(self.stage7ecbenc.encrypt(lolwut))
            if res == challenge:
                return msgs[stage] 
        elif stage == 8: #ecb copypasta

            res = self.sndrcv('encrypting your auth string... [{}]\r\nsupply an encrypted auth string to choose a user:'.format(self.stage8ecbenc.encrypt(pkcs7(connectiondata,16))))

            try:
                p = parsedata(self.stage8ecbenc.decrypt(res))
            except:
                return 'corrupted input:('
            out = 'attempting authentication... user:{},pass:{},admin:{}'.format(p[0],p[1],p[3])
            if p[3] == '1':
                out += '\r\n{}'.format(msgs[stage])
            else:
                out += '\r\ny u no admin??'
            return out

        elif stage == 9: #cbc flipping
            data = data.replace(';','').replace('=','')
            token = '<_token:comment=nice_user_lol;d={};type=cooldata>'.format(data)
            enc = AES.new(self.stage9cbckey,AES.MODE_CBC,self.stage9cbciv).encrypt(pkcs7(token,16))
            newtoken = self.sndrcv('encrypting morestuff: {}\r\ntoken: [{}]\r\nenter an encrypted token for authentication: '.format(token,enc))
            try:
                dec = AES.new(self.stage9cbckey,AES.MODE_CBC,self.stage9cbciv).decrypt(newtoken)
            except:
                return 'invalid token, decryption failed'
            if ';admin=true;' in dec:
                return dec+'\r\nhi admin!\r\n{}'.format(msgs[stage])
            else:
                return dec+'\r\nmissing ;admin=true; tag, permission denied!'
            
        elif stage == 10: #cbc padding oracle
            challenge = flags[stage]
            if data == challenge:
                return msgs[stage] #tbc
            enc = AES.new(self.stage10key,AES.MODE_CBC,self.stage10iv).encrypt(pkcs7(challenge,16))
            newmsg = self.sndrcv('secret: {}\r\ngive me some encrypted message plz?'.format([enc]))
            if newmsg == challenge:
                return msgs[stage] #temp..
            try:
                newmsg = AES.new(self.stage10cbckey,AES.MODE_CBC,self.stage10iv).decrypt(newmsg)
            except:
                return 'invalid input i think?? mrreoww:('
            if ispkcs7(newmsg):
                return 'nice message, om nom nom:)'
            else:
                return 'invalid padding, how rude!'
            
        elif stage==11:
            return "you are done here for now, congrats:) go find the bonus stage if you havn't done it yet.\r\n(hint:play with the connection string parameters)"
            
        else:
            pass

        return 'nope'
     
    def sndrcv(self,data):
        self.send(data)
        return self.receive()
    def receive(self):
        inc_data = self.conn.recv(32768)
        try:
            return inc_data.decode('base64')
        except:
            self.send('what do you want from me???')
            self.close()
    def send(self,data):
        return self.conn.send(data.encode('base64'))
    def close(self):
        self.conn.close()
        #add anon/bonus_id file cleanup maybe? might ruin some good solutions for the bonus stage so maybe not.

def rkey(length):
    return ''.join(chr(random.randint(0,255)) for i in range(length))
def pad0(st,n):
    return st+(n-(len(st)%n))*'\x00'
def pkcs7(st,n):
    l = (n - len(st)%n) % n
    return st + l*chr(l)
def ispkcs7(st):
    last = st[-1]
    if last*ord(last) == st[-ord(last):] and st[-ord(last)-1] != last:
        return 1
    else:
        return 0
def xor(st,key):
    return ''.join(chr(ord(st[i]) ^ ord(key[i%len(key)])) for i in range(len(st)))




def caesar(st,key):

    st = st.lower()
    st = ''.join(map(lambda x: string.ascii_lowercase[(ord(x)+key-97) % 26] if x.isalpha() else x, st))
    return st


def enc4(st,key):
    
    l=len(key)
    padding = (len(st) % l)
    split = [st[i::l] for i in range(l)]
    enc = [caesar(split[i],ord(key[i])-97)+'\x00'*(i - padding >= 0) for i in range(l)]
    res=''
    for i in range((len(st)-padding)/l+1):
        for j in range(l):
            res += enc[j][i]
    return res.replace('\x00','')


    
    
    

def lol(conn):
    s = session(conn)
    while 1:
        rcv = s.receive()
        #print 'rcv: %s' % rcv
        reply = s.dostuff(rcv)
        #print reply
        s.send(reply)
        

def __main__():
    a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        a.bind(((socket.gethostbyname(socket.gethostname()),0xf00d)))
    except:
        print 'socket open by another process'
        os.system('taskkill /f /im pythonw.exe')
        exit(0)

    a.listen(10)

    while 1:
        conn,o = a.accept()

        thread.start_new_thread(lol,(conn,))


    a.close()

if __name__=='__main__':
    __main__()
