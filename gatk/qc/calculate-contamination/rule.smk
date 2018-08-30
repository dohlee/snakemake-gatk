rule calculate_contamination:
    input:
        # Required arguments.
        pileup_summaries = '{sample}.pileupsummaries.table',
        # Optional arguments. Omit unused files.
    output:
        '{sample}.contamination.table'
    params:
        extra = ''
    threads: 1
    log: 'logs/gatk/calculate-contamination/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/qc/calculate-contamination'
