# Sample names for somatic PoNs.
PON_SAMPLES = ['normal1', 'normal2']

rule create_somatic_panel_of_normals:
    input:
        # Required input.
        # Try `expand`-ing your normal samples for PoN generation.
        expand('result/{sample}/{sample}.vcf.gz', sample=PON_SAMPLES)
    output:
        'pon.vcf.gz'
    params:
        # Optional parameters. Omit if unused.
        extra = ''
    threads: 1
    log: 'logs/gatk/create-somatic-panel-of-normals/PON.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/variant-filtering/create-somatic-panel-of-normals'
