from cnnClassifier import logger

from cnnClassifier.pipeline.stage_data_ingestion import DataIngestionPipeline


if __name__ == '__main__':
    try:
        logger.info("Data ingestion Pipeline Started")
        data_ingestion_pipeline=DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info("Data ingestion Pipeline successfully completed")
    except Exception as e:
        logger.error(f"An error occurred during data ingestion pipeline: {str(e)}")
        raise e

