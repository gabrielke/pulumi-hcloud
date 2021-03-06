# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class LoadBalancerNetwork(pulumi.CustomResource):
    enable_public_interface: pulumi.Output[bool]
    ip: pulumi.Output[str]
    load_balancer_id: pulumi.Output[float]
    network_id: pulumi.Output[float]
    def __init__(__self__, resource_name, opts=None, enable_public_interface=None, ip=None, load_balancer_id=None, network_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Hetzner Cloud Load Balancer Network to represent a private network on a Load Balancer in the Hetzner Cloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        lb1 = hcloud.LoadBalancer("lb1",
            load_balancer_type="lb11",
            network_zone="eu-central")
        mynet = hcloud.Network("mynet", ip_range="10.0.0.0/8")
        foonet = hcloud.NetworkSubnet("foonet",
            ip_range="10.0.1.0/24",
            network_id=mynet.id,
            network_zone="eu-central",
            type="cloud")
        srvnetwork = hcloud.LoadBalancerNetwork("srvnetwork",
            ip="10.0.1.5",
            load_balancer_id=lb1.id,
            network_id=mynet.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['enable_public_interface'] = enable_public_interface
            __props__['ip'] = ip
            if load_balancer_id is None:
                raise TypeError("Missing required property 'load_balancer_id'")
            __props__['load_balancer_id'] = load_balancer_id
            if network_id is None:
                raise TypeError("Missing required property 'network_id'")
            __props__['network_id'] = network_id
        super(LoadBalancerNetwork, __self__).__init__(
            'hcloud:index/loadBalancerNetwork:LoadBalancerNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, enable_public_interface=None, ip=None, load_balancer_id=None, network_id=None):
        """
        Get an existing LoadBalancerNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["enable_public_interface"] = enable_public_interface
        __props__["ip"] = ip
        __props__["load_balancer_id"] = load_balancer_id
        __props__["network_id"] = network_id
        return LoadBalancerNetwork(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
