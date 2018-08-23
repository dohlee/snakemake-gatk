rule mark_duplicates:
    input:
        '{sample}.bam'
    output:
        '{sample}.duplicates_marked.bam',
        # Optional arguments. Omit if unused.
        '{sample}.MarkDuplicates.metrics.txt'
    params:
        # Optional parameters. Omit if unused.
        java_options = '-Xmx4g'
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/preprocessing/mark-duplicates'
