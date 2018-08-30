# CollectReadCounts ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_CollectReadCounts.php))

count reads at specified intervals

## IO

- *{sample}*.bam, intervals.list -> *{sample}*.count.hdf5
- *{sample}*.bam, intervals.list -> *{sample}*.count.tsv

## Example snakemake rules
```python
rule collect_read_counts:
    input:
        # Required input.
        bam = '{sample}.bam',
        interval_list = 'intervals.list'
    output:
        # Required output in hdf5 or tsv format.
        '{sample}.counts.hdf5'
    params:
        # Optional parameters. Omit if unused.
        extra = '',
        interval_merging_rule = ''  # e.g. ALL / OVERLAPPING_ONLY
    threads: 1
    log: 'logs/gatk/collect_read_counts/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/coverage/collect_read_counts'
```
