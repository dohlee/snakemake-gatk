rule create_sequence_dictionary:
    input:
        '{reference}.fasta'
    output:
        '{reference}.fasta.dict'
    params:
        # Optional parameters. Omit if unused.
        java_options = '-Xmx4g'
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/misc/create_sequence_dictionary'
