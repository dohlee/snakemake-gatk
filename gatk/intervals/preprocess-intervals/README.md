# PreprocessIntervals ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_PreprocessIntervals.php))

prepare bins for coverage collection

## IO

- *{reference}*.fasta, intervals.list -> preprocessed.intervals.list
- *{reference}*.fasta -> preprocessed.intervals.list

## Example snakemake rules
```python
rule preprocess_interval:
    input:
        reference = 'reference/hg38.fasta'
    output:
        'preprocessed.intervals.list'
    params:
        # Optional parameters. Omit if unused.
        extra = '',
        interval_list = '',
        bin_length = '',
        padding = '',
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/intervals/preprocess-intervals'
```
