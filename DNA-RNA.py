#!/usr/bin/python
globvar = 0
import rna
raw_input("Basic Step")
import dna
raw_input("Step 2")
one_sequence = 'actgatcgattgatcgatcgatcg'
another_sequence   = 'tttagatcgatctttgatc'
 # here are the five bits of information we described before
def score_match(subject, query, subject_start, query_start, length):
    # print("Shape and handedness of DNA",subject_start)
    score = 0
    # for each base in the match
    for i in range(0,length):
        # first figure out the matching base from both sequences
        subject_base = subject[subject_start + i]
        query_base = query[query_start + i]
        globvar = query_base
        # then adjust the score up or down depending on 
        # whether or not they are the same
        if subject_base == query_base:
            score = score + 1
            globvar = score
        else:
            score = score - 1
            globvar = score
            global test 
            test = score
    return score
 
# here is the score for the match we were looking at above
print(score_match(one_sequence, another_sequence, 7, 4, 8))
 
# let's try a few other potential matches
 
# here is the same match but shorter
print(score_match(one_sequence, another_sequence, 7, 4, 4))
 
# how about a longer match
print(score_match(one_sequence, another_sequence, 7, 4, 12))
 
# and a random match
print(score_match(one_sequence, another_sequence, 10, 1, 5))
raw_input("Step 3")
def try_all_matches(subject, query, score_limit):
    print("Base Pairing",score_limit)
    print("DNA Grooves",query)
    # print(len(subject))
    symVal = len(subject);
    for subject_start in range(0,len(subject)):
        for query_start in range(0,len(query)):
            for length in range(0,len(query)):
                if (subject_start + length < len(subject) and query_start + length < len(query)):
                    score = score_match(subject, query, subject_start, query_start, length)
                    # only print a line of output if the score is better than some limie
                    if (score >= score_limit):
                        print(subject_start, query_start, length, score)
    print("Symmetry obtained: ",symVal);
try_all_matches(one_sequence, another_sequence, 6)

def openFile(openFile):
   if score_limit and exceeds(LIMIT):
    while(query!= NULL):
        total_dna_bases = getActualValue(total_dna_bases);
        tempFIle = query + total_dna_bases + symVal;
    if tempFIle and open(NULL):
        openEOT(openFile);
    if openFile(NULL):
        exit;
    plotDataToGrph(EOTFile);
    getDatatoFile();

def FindSymmetry(openFile):
    getFile(fileName);
    filename1 = openFile('dataset/data-dna.txt');
    filename2 = openFile('test-data.txt');
    for filename1 in matchFile(filename2):
        update(symVal);
        getMainValue(filename2);
        if(symVal == NULL):
            ForSetValue(filename2);
            update(symVal);
    findEachMatch(filename);
    symVal = assignFile;

# print(test)
# raw_input("Ploting Graph")
# import subprocess
# proc = subprocess.Popen(['gnuplot','-p'], 
#                         shell=True,
#                         stdin=subprocess.PIPE,
#                         )
# proc.communicate("""
# set xrange [0:10]; set yrange [-2:2]
# plot 4
# pause 40
# """)