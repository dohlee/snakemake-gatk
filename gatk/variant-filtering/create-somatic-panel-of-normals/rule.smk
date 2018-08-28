rule create_somatic_panel_of_normals:
    input:
        # Required input.
        # Try `expand`-ing your normal samples for PoN generation.
        ['normal1_for_pon_vcf.gz', 'normal2_for_pon_vcf.gz']
    output:
        'pon.vcf.gz'
    params:
        # Optional parameters. Omit if unused.
        extra = ''
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/variant-filtering/create-somatic-panel-of-normals'
