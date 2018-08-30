# MarkDuplicates (Picard) ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.4.0/picard_sam_markduplicates_MarkDuplicates.php))

identify duplicate reads arising from PCR amplification or resulting from incorrect detection of sequencing machine sensors.

## IO

- *{sample}*.bam -> *{sample}*.duplicates_marked.bam, *{sample}*.MarkDuplicates.metrics.txt

## Example snakemake rules

```python
rule mark_duplicates:
    input:
        '{sample}.bam'
    output:
        '{sample}.duplicates_marked.bam',
        # Optional arguments. Omit if unused.
        '{sample}.MarkDuplicates.metrics.txt'
    params:
        # Optional parameters. Omit if unused.
        extra = '-MAX_FILE_HANDLES 2000'
        java_options = '-Xmx32g'
    threads: 1
    log: 'logs/gatk/mark-duplicates/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/preprocessing/mark-duplicates'
```
