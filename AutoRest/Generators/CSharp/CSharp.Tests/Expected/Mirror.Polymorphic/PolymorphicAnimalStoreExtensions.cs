// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// 
// Code generated by Microsoft (R) AutoRest Code Generator 0.14.0.0
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.

namespace Fixtures.MirrorPolymorphic
{
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using System.Threading;
    using System.Threading.Tasks;
    using Microsoft.Rest;
    using Models;

    public static partial class PolymorphicAnimalStoreExtensions
    {
            /// <summary>
            /// Product Types
            /// </summary>
            /// The Products endpoint returns information about the Uber products offered
            /// at a given location. The response includes the display name and other
            /// details about each product, and lists the products in the proper display
            /// order.
            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='animalCreateOrUpdateParameter'>
            /// An Animal
            /// </param>
            public static Animal CreateOrUpdatePolymorphicAnimals(this IPolymorphicAnimalStore operations, Animal animalCreateOrUpdateParameter = default(Animal))
            {
                return Task.Factory.StartNew(s => ((IPolymorphicAnimalStore)s).CreateOrUpdatePolymorphicAnimalsAsync(animalCreateOrUpdateParameter), operations, CancellationToken.None, TaskCreationOptions.None, TaskScheduler.Default).Unwrap().GetAwaiter().GetResult();
            }

            /// <summary>
            /// Product Types
            /// </summary>
            /// The Products endpoint returns information about the Uber products offered
            /// at a given location. The response includes the display name and other
            /// details about each product, and lists the products in the proper display
            /// order.
            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='animalCreateOrUpdateParameter'>
            /// An Animal
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task<Animal> CreateOrUpdatePolymorphicAnimalsAsync( this IPolymorphicAnimalStore operations, Animal animalCreateOrUpdateParameter = default(Animal), CancellationToken cancellationToken = default(CancellationToken))
            {
                var _result = await operations.CreateOrUpdatePolymorphicAnimalsWithHttpMessagesAsync(animalCreateOrUpdateParameter, null, cancellationToken).ConfigureAwait(false);
                return _result.Body;
            }

    }
}
