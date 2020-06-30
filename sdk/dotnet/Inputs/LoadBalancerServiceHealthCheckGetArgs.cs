// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.HCloud.Inputs
{

    public sealed class LoadBalancerServiceHealthCheckGetArgs : Pulumi.ResourceArgs
    {
        [Input("http")]
        public Input<Inputs.LoadBalancerServiceHealthCheckHttpGetArgs>? Http { get; set; }

        [Input("interval", required: true)]
        public Input<int> Interval { get; set; } = null!;

        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        [Input("retries")]
        public Input<int>? Retries { get; set; }

        [Input("timeout", required: true)]
        public Input<int> Timeout { get; set; } = null!;

        public LoadBalancerServiceHealthCheckGetArgs()
        {
        }
    }
}
