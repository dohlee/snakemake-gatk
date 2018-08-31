rule select_variants:
    input:
        # Required input.
        vcf = '{input}.vcf.gz',
    output:
        # Required output. You may change output name as you want.
        '{input}.selected.vcf.gz'
    params:
        # Optional parameters. Omit if unused.
        select_type_to_include = '',  # Type of variants goes here. e.g. INDEL, SNP, MIXED, MNP, SYMBOLIC, NO_VARIATION
        select_type_to_exclude = '',  # Type of variants goes here. e.g. INDEL, SNP, MIXED, MNP, SYMBOLIC, NO_VARIATION
        restrict_alleles_to = '',  # Select only variants of a particular allelicity.
        intervals = '',  # One or more genomics intervals over which to operate.
        extra = ''
    threads: 1
    log: 'logs/gatk/select-variants/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/variant-manipulation/select-variants'
