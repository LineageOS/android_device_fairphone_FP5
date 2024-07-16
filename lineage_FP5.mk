#
# SPDX-FileCopyrightText: 2021-2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from FP5 device
$(call inherit-product, device/fairphone/FP5/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Boot animation
TARGET_SCREEN_HEIGHT := 2700
TARGET_SCREEN_WIDTH := 1224

# Device identifier. This must come after all inclusions.
PRODUCT_NAME := lineage_FP5
PRODUCT_DEVICE := FP5
PRODUCT_BRAND := Fairphone
PRODUCT_MODEL := FP5
PRODUCT_MANUFACTURER := Fairphone

PRODUCT_SYSTEM_NAME := FP5

PRODUCT_GMS_CLIENTID_BASE := android-alcatel

PRODUCT_BUILD_PROP_OVERRIDES += \
    TARGET_PRODUCT=$(PRODUCT_SYSTEM_NAME)

BUILD_FINGERPRINT := Fairphone/FP5/FP5:14/UKQ1.230924.001/UT20:user/release-keys
