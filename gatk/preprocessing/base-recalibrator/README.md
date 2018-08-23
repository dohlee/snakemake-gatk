# BaseRecalibrator ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_BaseRecalibrator.php))

generate recalibration table for Base Quality Score Recalibration (BQSR).

## IO

- *{sample}*.bam, *{reference}*.fasta, ['*{sites_of_variation}*.vcf', '*{sites_of_variation2}*.vcf'] -> recalibrated_data

## Example snakemake rules
```python
rule base_recalibrator:
    input:
        # Required input.
        bam = '{sample}.bam',
        reference = '{reference}.fasta',
        known_sites = ['sites_of_variation.vcf', 'sites_of_variation2.vcf'],
    output:
        # Required output.
        'recalibrated_data.table'
    threads: 1
    wrapper: 'http://dohlee-bio.info:9193/gatk/preprocessing/base-recalibrator'

```
