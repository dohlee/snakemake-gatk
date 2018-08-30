# CalculateContamination ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_contamination_CalculateContamination.php))

how many fractions of reads are coming from cross-sample contamination?

## IO

- *{sample}*.pileupsummaries.table -> *{sample}*.contamination.table

## Example snakemake rules

```python
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
```
