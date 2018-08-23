# IndexFeatureFile ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.3.0/org_broadinstitute_hellbender_tools_IndexFeatureFile.php))

create an index for a feature file, e.g. VCF or BED file.

## IO

- *{sample}*.vcf -> *{sample}*.vcf.tbi

## Example snakemake rules

```python
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
```
