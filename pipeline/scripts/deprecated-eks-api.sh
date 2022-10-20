# What is Pluto?
# Pluto is a tool developed by FairwindsOps which helps in detecting deprecated kubernetes APIs used in your code repositories and helm releases.

# Pluto Installation on Mac
brew install FairwindsOps/tap/pluto

# How to detects deprecated APIs in Helm charts installed on your cluster?
pluto detect-helm


# How to detects deprecated APIs in Helm charts in your repository?
helm3 template vertical-pod-autoscaler | pluto detect
helm3 template vertical-pod-autoscaler | pluto detect -o wide --target-versions k8s=v1.20 -

# How to detects deprecated APIs in all Helm charts in your repository using a for loop?

cd pipeline/helm/charts
 
for i in $(ls)
do
  echo -e "--------------------------------------------------------------------------------------------------"
  echo "Checking deprecated for $i Helm chart: "
  helm3 template $i | pluto detect -o wide --target-versions k8s=v1.21 -
  echo -e "--------------------------------------------------------------------------------------------------\n\n"
done