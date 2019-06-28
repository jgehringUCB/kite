import os
from collections import OrderedDict



def make_mismatch_map(FeatureDict):
    odict = OrderedDict()
    counter=0
    for item in input_tags:
        name=(item)
        seq=tags[item]
        if counter == 0:
            feature_barcode_length = len(seq)
            print("Feature Barcode Length: "+str(feature_barcode_length)+'\n')
            print('Read the following tags:')
            counter+=1
        print(name)
        print(seq)
        odict[name+'-*-*'] = str(seq)[:feature_barcode_length]
        for pos in range(feature_barcode_length):
            letter =str(seq)[pos]
            barcode=list(str(seq)[:feature_barcode_length])
            if letter=='A':
                barcode[pos]='T'
                odict[name+'-'+str(pos)+'-1'] = "".join(barcode)
                barcode[pos]='G'
                odict[name+'-'+str(pos)+'-2'] = "".join(barcode)
                barcode[pos]='C'
                odict[name+'-'+str(pos)+'-3'] = "".join(barcode)
            elif letter=='G':
                barcode[pos]='T'
                odict[name+'-'+str(pos)+'-1'] = "".join(barcode)
                barcode[pos]='A'
                odict[name+'-'+str(pos)+'-2'] = "".join(barcode)
                barcode[pos]='C'
                odict[name+'-'+str(pos)+'-3'] = "".join(barcode)
            elif letter=='C':
                barcode[pos]='T'
                odict[name+'-'+str(pos)+'-1'] = "".join(barcode)
                barcode[pos]='G'
                odict[name+'-'+str(pos)+'-2'] = "".join(barcode)
                barcode[pos]='A'
                odict[name+'-'+str(pos)+'-3'] = "".join(barcode)
            else:
                barcode[pos]='A'
                odict[name+'-'+str(pos)+'-1'] = "".join(barcode)
                barcode[pos]='G'
                odict[name+'-'+str(pos)+'-2'] = "".join(barcode)
                barcode[pos]='C'
                odict[name+'-'+str(pos)+'-3'] = "".join(barcode)
                
    return odict


def write_files(tag_map, mismatch_t2g_path, mismatch_fasta_path):
    tagmap_file = open(tagmap_file_path, "w+")
    tagmap_fasta = open(tagmap_fasta_path, "w+")
    for i in list(tag_map.keys()):
        if i[-4:]=='-*-*':
            #print(i[:-4]+'\t'+i[:-4]+'\t'+i[:-4])
            tagmap_file.write(i[:-4]+'\t'+i[:-4]+'\t'+i[:-4]+'\n')
            tagmap_fasta.write(">" + i[:-4] + "\n" +tag_map[i] + "\n")
        else:
            #print(i+'\t'+'-'.join(i.split('-')[:-2])+'\t'+'-'.join(i.split('-')[:-2]))
            tagmap_file.write(i+'\t'+'-'.join(i.split('-')[:-2])+'\t'+'-'.join(i.split('-')[:-2])+'\n')
            tagmap_fasta.write(">" + i + "\n" +tag_map[i] + "\n")
    tagmap_file.close()
    tagmap_fasta.close()
    

def kite_mismatch_maps(FeatureDict, mismatch_t2g_path, mismatch_fasta_path):
    write_files(parse_tags(get_tags(FeatureDict)), mismatch_file_path, mismatch_fasta_path)
