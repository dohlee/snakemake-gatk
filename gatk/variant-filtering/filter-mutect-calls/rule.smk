rule filter_mutect_calls:
    input:
        # Required input.
        vcf = '{sample}.vcf.gz',
        contamination_table = '{sample}.contamination.table',
    output:
        '{sample}.oncefiltered.vcf.gz'
    params:
        # Optional parameters. Omit if unused.
        extra = ''
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/variant-filtering/filter-mutect-calls'
