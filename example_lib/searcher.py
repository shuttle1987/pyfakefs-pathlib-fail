def determine_labels(tgt_dir, label_type):
    """ Returns a set of phonemes found in the corpus. """

    label_dir = os.path.join(tgt_dir, "label/")
    if not os.path.isdir(label_dir):
        raise FileNotFoundError(
            "The directory {} does not exist.".format(tgt_dir))

    phonemes = set()
    for fn in os.listdir(label_dir):
        if fn.endswith(label_type):
            with open(join(label_dir, fn)) as f:
                try:
                    line_phonemes = set(f.readline().split())
                except UnicodeDecodeError:
                    logger.error("Unicode decode error on file %s", fn)
                    print("Unicode decode error on file {}".format(fn))
                    raise
                phonemes = phonemes.union(line_phonemes)
    return phonemes

