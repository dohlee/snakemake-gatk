rule create_sequence_dictionary:
    input:
        '{reference}.fasta'
    output:
        '{reference}.fasta.dict'
    params:
        # Optional parameters. Omit if unused.
        java_options = '-Xmx4g'
    threads: 1
    resources: RAM = 4
    log: 'logs/gatk/create-sequence-dictionary/{reference}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/reference/create_sequence_dictionary'
