# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReconfigurationInformation(Model):
    """Information about current reconfiguration like phase, type, previous
    configuration role of replica and reconfiguration start date time.

    :param previous_configuration_role: Replica role before reconfiguration
     started. Possible values include: 'Unknown', 'None', 'Primary',
     'IdleSecondary', 'ActiveSecondary'
    :type previous_configuration_role: str or
     ~azure.servicefabric.models.ReplicaRole
    :param reconfiguration_phase: Current phase of ongoing reconfiguration. If
     no reconfiguration is taking place then this value will be "None".
     Possible values include: 'Unknown', 'None', 'Phase0', 'Phase1', 'Phase2',
     'Phase3', 'Phase4', 'AbortPhaseZero'
    :type reconfiguration_phase: str or
     ~azure.servicefabric.models.ReconfigurationPhase
    :param reconfiguration_type: Type of current ongoing reconfiguration. If
     no reconfiguration is taking place then this value will be "None".
     Possible values include: 'Unknown', 'SwapPrimary', 'Failover', 'Other'
    :type reconfiguration_type: str or
     ~azure.servicefabric.models.ReconfigurationType
    :param reconfiguration_start_time_utc: Start time (in UTC) of the ongoing
     reconfiguration. If no reconfiguration is taking place then this value
     will be zero date-time.
    :type reconfiguration_start_time_utc: datetime
    """

    _attribute_map = {
        'previous_configuration_role': {'key': 'PreviousConfigurationRole', 'type': 'str'},
        'reconfiguration_phase': {'key': 'ReconfigurationPhase', 'type': 'str'},
        'reconfiguration_type': {'key': 'ReconfigurationType', 'type': 'str'},
        'reconfiguration_start_time_utc': {'key': 'ReconfigurationStartTimeUtc', 'type': 'iso-8601'},
    }

    def __init__(self, previous_configuration_role=None, reconfiguration_phase=None, reconfiguration_type=None, reconfiguration_start_time_utc=None):
        super(ReconfigurationInformation, self).__init__()
        self.previous_configuration_role = previous_configuration_role
        self.reconfiguration_phase = reconfiguration_phase
        self.reconfiguration_type = reconfiguration_type
        self.reconfiguration_start_time_utc = reconfiguration_start_time_utc
