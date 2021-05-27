rule add_or_replace_read_groups:
    input:
        # Required arguments.
        '{sample}.sorted.bam',
        # Optional arguments. Omit unused files.
    output:
        '{sample}.reheadered.sorted.bam',
    params:
        java_options = '-Xmx4g',
        extra = '',
        # --RGLB / -LB option.
        read_group_library = lambda wildcards: wildcards.sample,
        # --RGPL / -PL option.
        read_group_platform = 'illumina',
        # --RGPU / -PU option.
        read_group_platform_unit = 'run',
        # --RGSM / -SM option.
        read_group_sample_name = lambda wildcards: wildcards.sample,
    threads: 1
    resources: RAM = 4
    log: 'logs/gatk/add_or_replace_read_groups/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/picard/add-or-replace-read-groups'
