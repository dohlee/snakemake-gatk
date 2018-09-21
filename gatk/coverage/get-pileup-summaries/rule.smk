rule get_pileup_summaries:
    input:
        # Required arguments.
        bam = '{sample}.bam',
        common_biallelic_variants = 'resources/small_exac_common_3.hg38.vcf.gz'
        # Optional arguments. Omit unused files.
    output:
        '{sample}.pileupsummaries.table'
    params:
        java_options = '-Xmx4g',
        extra = '',
    threads: 1
    resources: RAM = 4
    log: 'logs/gatk/get-pileup-summaries/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/coverage/get-pileup-summaries'
