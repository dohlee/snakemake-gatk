rule mark_duplicates:
    input:
        bam = '{sample}.bam',
        reference = '{reference}.fasta',
        recalibration_table = '{sample}_recalibration.table',
    output:
        '{sample}.recalibrated.bam'
    params:
        # Optional parameters. Omit if unused.
        java_options = '-Xmx32g'
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/preprocessing/apply-bqsr'
