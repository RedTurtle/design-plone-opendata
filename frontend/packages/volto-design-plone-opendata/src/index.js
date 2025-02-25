import { OpendataDatasetView } from './components/views';

const applyConfig = (config) => {

  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    'OpendataDataset': OpendataDatasetView, 
  };

  return config;
};

export default applyConfig;
