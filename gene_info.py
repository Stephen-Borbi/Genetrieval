from Bio import Entrez

def get_gene_info(query):
    Entrez.email = 'steborb6@gmail.com'  # Replace with your own email address
    handle = Entrez.esearch(db='gene', term=query)
    record = Entrez.read(handle)
    if record['Count'] == '0':
        return None
    gene_id = record['IdList'][0]
    handle = Entrez.efetch(db='gene', id=gene_id, retmode='xml')
    record = Entrez.read(handle)
    gene_info = record[0]
    return gene_info