rule mutect2_tumor_only:
    input:
        # Required arguments.
        reference = 'reference/Homo_sapiens_assembly38.fasta',
        bam = '{sample}.bam',
        bam_idx = '{sample}.bam.bai',
        reference_dict = 'reference/Homo_sapiens_assembly38.dict'
        # Optional arguments. Omit unused files.
    output:
        '{sample}.vcf.gz'
    params:
        extra = '--disable-read-filter MateOnSameContigOrNoMappedMateReadFilter '
    threads: 1
    log: 'logs/gatk/mutect2-tumor-only/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/mutect2/tumor-only'
