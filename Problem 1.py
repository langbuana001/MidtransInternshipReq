#Problem 1 -- String simmilarities
#We can use this function to measure degree of simmilarities betweeen address and spot potential error.
#The higher degree of simmilarities, the bigger the chance for human error


street_address = ["PERUM. PURI ARSANA JL. RAYA CIPUTAT PARUNG KM.11 E-12 IDN",
                  "Jalan budi mulia gang F3 No.29D Rt.04 Rw.02, Jakarta Selatan. Indonesia.",
                  "Level 1, Tower 6, Avenue 3, The Horizon, Bangsar South, No. 4, Jalan Kerinchi",
                  "Jalan budi mulia Gg. F2 Nomor 29 D RT. 04 Rw.02, JakSel.",
                  "Green garden M17A no.44 Jakarta Barat - 11520",
                  "Jln budi mulia Gg. F2 Nomor 28 D RT. 04 Rw.02, JakSel. IDN.",
                  "Jl BudiMulia Gang f2 Nomor 28 D RT. 04/02, Jakarta Selatan. IDN. "]

abbreviations = {
                    "jl": "jalan",
                    "jln": "jalan",
                    "jalan": "jalan",
                    "perum": "perumahan",
                    "perumahan": "perumahan",
                    "jak": "jakarta",
                    "jkt": "jakarta",
                    "jaksel": "jakartaselatan",
                    "jaktim": "jakartatimur",
                    "jakpus": "jakartapusat",
                    "jakbar": "jakartabarat",
                    "jakut": "jakartautara",
                    "idn": "indonesia",
                    "id": "indonesia",
                    "/": "rw",
                    "no": "nomor",
                    "gang": "gang",
                    "gg": "gang"
                }

#Assume we were given two address
#The function simmilarities() takes two input string1 and string 2
#String1 shall be the target comparator, String2 shall be the subject of comparison
def simmilarities(string1, string2):

    #We want to keep things very conservative. There might be diffrences
    #   in writing style but we want to eliminate all potential error
    #Let us transform our input string to eliminate unnecessary characters 
    string1 = transform(string1)
    string2 = transform(string2)

    
    #Let us calculate the simmilarities percentage
    simmilar = 0

    for x,y in zip(string1,string2):
        if x == y:
            simmilar += 1
            
    percentage = simmilar / len(string1) * 100.0 
    
    return percentage

    
def transform(string):
    string = string.lower().replace(".", " ").replace(",", "").replace("/", " rw ")
    final_word = ""
    for word in string.split():
        if word in abbreviations:
            final_word = final_word + abbreviations[word] + " "
        else:
            final_word = final_word + word + " "
            
    return final_word

#TEST
print("There are", simmilarities(street_address[0], street_address[6]), "percent simmilarities between",street_address[0], "and", street_address[6] )
print("There are", simmilarities(street_address[1], street_address[6]), "percent simmilarities between",street_address[1], "and", street_address[6] )
print("There are", simmilarities(street_address[2], street_address[5]), "percent simmilarities between",street_address[2], "and", street_address[5] )
print("There are", simmilarities(street_address[3], street_address[2]), "percent simmilarities between",street_address[3], "and", street_address[2] )
print("There are", simmilarities(street_address[1], street_address[5]), "percent simmilarities between",street_address[1], "and", street_address[5] )

















