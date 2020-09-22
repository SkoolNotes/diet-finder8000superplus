#cat data_uniprot-reviewed.fasta | sed -E 's/^>.+OS\=([a-zA-Z0-9:\/ \.\(\)-]+)=.+/>\1/g' | ack '\|'
cat data_uniprot-reviewed.fasta | sed -E 's/^>.+OS\=([^=]+)=.+/>\1/g' > data_processed.txt

