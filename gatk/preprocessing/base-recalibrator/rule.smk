rule base_recalibrator:
    input:
        # Required input.
        bam = '{sample}.bam',
        reference = '{reference}.fasta',
        known_sites = ['sites_of_variation.vcf', 'sites_of_variation2.vcf'],
    output:
        # Required output.
        '{sample}_recalibration.table'
    threads: 1
    log: 'logs/gatk/base-recalibrator/{sample}.log'
    wrapper: 'http://dohlee-bio.info:9193/gatk/preprocessing/base-recalibrator'
