# -*- coding: utf-8 -*-
import sys
def read_csv(csvfile: str) -> list:
    ''' Read a csv file and output the columns and records'''
    with open(csvfile,'r') as csv:
        csv_content=csv.readlines()
        
    columns=csv_content[0].strip().split(',')
    content=csv_content[1:]
    records=[]
    for row in content:
        values = row.strip().split(',')
        record = { col.lower(): values[n] for n, col in enumerate(columns) }    
        records.append(record)
    
    return records  

def find_top_mark_records(records : list) -> list: 
    ''' Find the records containing the top marks'''    
    records.sort(key = lambda r: float(r['score']), reverse=True)    
    top_mark = records[0]['score']
    top_mark_records = filter(lambda x: x['score'] == top_mark, records)
    return list(top_mark_records)

def output_top_mark_records(top_mark_records : list):
    '''Print the top mark records to STDOUT in alphabetical order'''
    top_mark_records.sort(key = lambda x: (x['first name'],x['second name']))
    for rec in top_mark_records:
        print(f"{rec['first name']} {rec['second name']}\n")
        
    print(f"Score: {top_mark_records[0]['score']}")

if __name__=='__main__':
    
    csv_file_to_parse = sys.argv[1]
    records = read_csv(csv_file_to_parse)
    top_mark_records = find_top_mark_records(records)
    output_top_mark_records(top_mark_records)
