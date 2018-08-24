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
    wrapper:
        'http://dohlee-bio.info:9193/gatk/coverage/collect_read_counts'
