rule mark_duplicates:
    input:
        '{sample}.bam'
    output:
        '{sample}.duplicates_marked.bam',
        # Optional arguments. Omit if unused.
        '{sample}.MarkDuplicates.metrics.txt'
    params:
        # Optional parameters. Omit if unused.
        extra = '-MAX_FILE_HANDLES 2000'
        java_options = '-Xmx32g'
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/preprocessing/mark-duplicates'
