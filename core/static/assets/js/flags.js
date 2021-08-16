// Import Rollout SDK
import * as Rox from 'rox-browser';

// Create a Roxflag in the flags container class
const Flags = {
  enableCustomersKPI: new Rox.Flag(false),
  // list of all dashboard options - here we give the engn team the option to revert
  enableLineGraph: new Rox.Variant('is-newversion', ['is-revert', 'is-newversion']),
  enableRevenueKPI: new Rox.Flag(false),
  // enableLineGraph: new Rox.Flag(false),
  enableNewTaskButton: new Rox.Flag(false),
};

export const configurationFetchedHandler = fetcherResults => {
  if (fetcherResults.hasChanges && fetcherResults.fetcherStatus === 'APPLIED_FROM_NETWORK') {
    window.location.reload(false)
  }
}

async function initCloudBees() {
  const options = {
    configurationFetchedHandler: configurationFetchedHandler
  }

  // Register the flags with Rollout
  Rox.register('ReleaseV1', Flags);

  // Setup the Rollout key
  await Rox.setup('60fef08497b721ffee72cea8', options);

}

initCloudBees().then(function () {
  console.log('Done loading CloudBees Feature Management')
})


