# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
from . import transforms_vg_bp as TBP


def build_transforms(cfg, is_train=True):
    if is_train:
        min_size = cfg.INPUT.MIN_SIZE_TRAIN
        max_size = cfg.INPUT.MAX_SIZE_TRAIN
        # flip_prob = 0.5  # cfg.INPUT.FLIP_PROB_TRAIN
        flip_prob = 0
    else:
        min_size = cfg.INPUT.MIN_SIZE_TEST
        max_size = cfg.INPUT.MAX_SIZE_TEST
        flip_prob = 0

    to_bgr255 = cfg.INPUT.TO_BGR255
    normalize_transform = TBP.Normalize(
        mean=cfg.INPUT.PIXEL_MEAN, std=cfg.INPUT.PIXEL_STD, to_bgr255=to_bgr255
    )

    To255 = TBP.To255(mean=cfg.INPUT.PIXEL_MEAN, std=cfg.INPUT.PIXEL_STD, to_bgr255=to_bgr255)

    transform = TBP.Compose(
        [
            TBP.ResizeAndNormalize(min_size, max_size, cfg.INPUT.PIXEL_MEAN, cfg.INPUT.PIXEL_STD),
            TBP.ToTensor(),
        ]
    )
    return transform
