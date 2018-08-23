rule index_feature_file:
    input:
        '{sample}.vcf'
    output:
        '{sample}.vcf.tbi'
    params:
        # Optional parameters. Omit if unused.
        java_options = '-Xmx4g'
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/misc/index-feature-file'
