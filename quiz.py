print('\n\n\nWelkom bij de Quiz van het jaar!')

antwoord=input('Ben je klaar om te spelen??:')
punten=0
aantal_vragen=3

def is_valide_speler(speler):
    namen = ['Daan']
    for naam in namen:
        if naam==speler.lower(): 
            return True
    return False

if antwoord.lower()=='ja':
 
   naamantwoord=input('Geef je naam op')
   check_valide_speler=is_valide_speler(naamantwoord)
   if check_valide_speler:

     print('\n\nDaar gaan we!\nGeef bij iedere vraag het juiste antwoord(GEEN HOOFDLETTERS).\n\n')

     antwoord=input('Vraag 1: Wat voor eten koopt max het meest in de pauze?\n')
     if antwoord.lower()=='frikandelbroodje' or antwoord.lower()=='energy drink':
        punten += 1
        print('goed!')
     else:
        print('fout!')
 
     antwoord=input('Vraag 2: Wat voor laptop heeft max?\n')
     if antwoord.lower()=='MSI':
        punten += 1
        print('goed')
     else:
        print('fout')

     antwoord=input('Vraag 3: Hoe oud wordt Max volgend jaar?\n')
     if antwoord.lower()=='19' or antwoord.lower()=='negentien':
        punten += 1
        print('goed')
     else:
        print('fout')
    
     cijfer = round(float(3/aantal_vragen*punten), 1)
     print('Je bent klaar! Bedankt voor het spelen.:'+str(cijfer)+'.')
     if punten >= 2: print('Lekker bezgig!')
     else: print('doeeeg!!\n\n')

   else:
      print('false')

elif antwoord.lower()=='nee':
   print('ok, bye!')