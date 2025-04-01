#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/fairphone/FP5',
    'hardware/qcom-caf/sm8350',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'libmmosal',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/bin/wfdservice': blob_fixup()
        .add_needed('libwfdservice_shim.so'),
    'system_ext/lib/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/lib/libwfdservice.so': blob_fixup()
        .replace_needed('android.media.audio.common.types-V2-cpp.so', 'android.media.audio.common.types-V4-cpp.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .replace_needed('android.hidl.base@1.0.so', 'libhidlbase.so')
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so'),
    'vendor/etc/libnfc-hal-st.conf': blob_fixup()
        .regex_replace('STNFC_HAL_LOGLEVEL=.*', 'STNFC_HAL_LOGLEVEL=0x12'),
    'vendor/lib64/hw/fingerprint.lahaina.so': blob_fixup()
        .fix_soname(),
    'vendor/lib64/libmorpho_movie_stabilizer.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_acquire')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'FP5',
    'fairphone',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
