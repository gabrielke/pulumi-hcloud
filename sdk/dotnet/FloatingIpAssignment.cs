// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.HCloud
{
    /// <summary>
    /// Provides a Hetzner Cloud Floating IP Assignment to assign a Floating IP to a Hetzner Cloud Server. Deleting a Floating IP Assignment will unassign the Floating IP from the Server.
    /// 
    /// ## Example Usage
    /// 
    /// 
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using HCloud = Pulumi.HCloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var node1 = new HCloud.Server("node1", new HCloud.ServerArgs
    ///         {
    ///             Datacenter = "fsn1-dc8",
    ///             Image = "debian-9",
    ///             ServerType = "cx11",
    ///         });
    ///         var master = new HCloud.FloatingIp("master", new HCloud.FloatingIpArgs
    ///         {
    ///             HomeLocation = "nbg1",
    ///             Type = "ipv4",
    ///         });
    ///         var main = new HCloud.FloatingIpAssignment("main", new HCloud.FloatingIpAssignmentArgs
    ///         {
    ///             FloatingIpId = master.Id,
    ///             ServerId = node1.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class FloatingIpAssignment : Pulumi.CustomResource
    {
        [Output("floatingIpId")]
        public Output<int> FloatingIpId { get; private set; } = null!;

        [Output("serverId")]
        public Output<int> ServerId { get; private set; } = null!;


        /// <summary>
        /// Create a FloatingIpAssignment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FloatingIpAssignment(string name, FloatingIpAssignmentArgs args, CustomResourceOptions? options = null)
            : base("hcloud:index/floatingIpAssignment:FloatingIpAssignment", name, args ?? new FloatingIpAssignmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FloatingIpAssignment(string name, Input<string> id, FloatingIpAssignmentState? state = null, CustomResourceOptions? options = null)
            : base("hcloud:index/floatingIpAssignment:FloatingIpAssignment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FloatingIpAssignment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FloatingIpAssignment Get(string name, Input<string> id, FloatingIpAssignmentState? state = null, CustomResourceOptions? options = null)
        {
            return new FloatingIpAssignment(name, id, state, options);
        }
    }

    public sealed class FloatingIpAssignmentArgs : Pulumi.ResourceArgs
    {
        [Input("floatingIpId", required: true)]
        public Input<int> FloatingIpId { get; set; } = null!;

        [Input("serverId", required: true)]
        public Input<int> ServerId { get; set; } = null!;

        public FloatingIpAssignmentArgs()
        {
        }
    }

    public sealed class FloatingIpAssignmentState : Pulumi.ResourceArgs
    {
        [Input("floatingIpId")]
        public Input<int>? FloatingIpId { get; set; }

        [Input("serverId")]
        public Input<int>? ServerId { get; set; }

        public FloatingIpAssignmentState()
        {
        }
    }
}