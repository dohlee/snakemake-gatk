rule preprocess_interval:
    input:
        reference = 'reference/hg38.fasta'
    output:
        'preprocessed.intervals.list'
    params:
        # Optional parameters. Omit if unused.
        extra = '',
        interval_list = '',
        bin_length = '',
        padding = '',
    threads: 1
    log: 'logs/gatk/preprocess-interval/preprocessed.intervals.list.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/intervals/preprocess-intervals'
