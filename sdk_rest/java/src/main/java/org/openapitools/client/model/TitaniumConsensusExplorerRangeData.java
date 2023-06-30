/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.TitaniumChartRanges;
import org.openapitools.client.model.TitaniumRangePoint;
import org.openapitools.client.model.TitaniumTradePeriodsWithMetrics;
import org.openapitools.client.model.TitaniumTradeRangesData;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumConsensusExplorerRangeData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-06-30T14:58:59.766741Z[UTC]")
public class TitaniumConsensusExplorerRangeData {
  public static final String SERIALIZED_NAME_ALL_PARTICIPANT_CRS_CONSENSUS_PRICE = "allParticipantCrsConsensusPrice";
  @SerializedName(SERIALIZED_NAME_ALL_PARTICIPANT_CRS_CONSENSUS_PRICE)
  private TitaniumRangePoint allParticipantCrsConsensusPrice;

  public static final String SERIALIZED_NAME_BIMODAL_LEFT_MEAN = "bimodalLeftMean";
  @SerializedName(SERIALIZED_NAME_BIMODAL_LEFT_MEAN)
  private TitaniumRangePoint bimodalLeftMean;

  public static final String SERIALIZED_NAME_BIMODAL_RIGHT_MEAN = "bimodalRightMean";
  @SerializedName(SERIALIZED_NAME_BIMODAL_RIGHT_MEAN)
  private TitaniumRangePoint bimodalRightMean;

  public static final String SERIALIZED_NAME_CHALLENGE_OVERLAY_CRS_CONSENSUS_PRICE = "challengeOverlayCrsConsensusPrice";
  @SerializedName(SERIALIZED_NAME_CHALLENGE_OVERLAY_CRS_CONSENSUS_PRICE)
  private TitaniumRangePoint challengeOverlayCrsConsensusPrice;

  public static final String SERIALIZED_NAME_CHART_RANGES = "chartRanges";
  @SerializedName(SERIALIZED_NAME_CHART_RANGES)
  private TitaniumChartRanges chartRanges;

  public static final String SERIALIZED_NAME_EVP_MID = "evpMid";
  @SerializedName(SERIALIZED_NAME_EVP_MID)
  private TitaniumRangePoint evpMid;

  public static final String SERIALIZED_NAME_EXPERT_POST_CHALLENGE_CONSENSUS_PRICE = "expertPostChallengeConsensusPrice";
  @SerializedName(SERIALIZED_NAME_EXPERT_POST_CHALLENGE_CONSENSUS_PRICE)
  private TitaniumRangePoint expertPostChallengeConsensusPrice;

  public static final String SERIALIZED_NAME_EXPERT_PRE_CHALLENGE_CONSENSUS_PRICE = "expertPreChallengeConsensusPrice";
  @SerializedName(SERIALIZED_NAME_EXPERT_PRE_CHALLENGE_CONSENSUS_PRICE)
  private TitaniumRangePoint expertPreChallengeConsensusPrice;

  public static final String SERIALIZED_NAME_MARKET_DATA_CRS_CONSENSUS_PRICE = "marketDataCrsConsensusPrice";
  @SerializedName(SERIALIZED_NAME_MARKET_DATA_CRS_CONSENSUS_PRICE)
  private TitaniumRangePoint marketDataCrsConsensusPrice;

  public static final String SERIALIZED_NAME_SUBMISSION_MEAN_POINT = "submissionMeanPoint";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_MEAN_POINT)
  private TitaniumRangePoint submissionMeanPoint;

  public static final String SERIALIZED_NAME_SUBMISSION_POINT = "submissionPoint";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_POINT)
  private TitaniumRangePoint submissionPoint;

  public static final String SERIALIZED_NAME_TRADE_PERIODS_WITH_METRICS = "tradePeriodsWithMetrics";
  @SerializedName(SERIALIZED_NAME_TRADE_PERIODS_WITH_METRICS)
  private TitaniumTradePeriodsWithMetrics tradePeriodsWithMetrics;

  public static final String SERIALIZED_NAME_TRADE_RANGES_DATA = "tradeRangesData";
  @SerializedName(SERIALIZED_NAME_TRADE_RANGES_DATA)
  private TitaniumTradeRangesData tradeRangesData;

  public TitaniumConsensusExplorerRangeData() { 
  }

  public TitaniumConsensusExplorerRangeData allParticipantCrsConsensusPrice(TitaniumRangePoint allParticipantCrsConsensusPrice) {
    
    this.allParticipantCrsConsensusPrice = allParticipantCrsConsensusPrice;
    return this;
  }

   /**
   * Get allParticipantCrsConsensusPrice
   * @return allParticipantCrsConsensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getAllParticipantCrsConsensusPrice() {
    return allParticipantCrsConsensusPrice;
  }


  public void setAllParticipantCrsConsensusPrice(TitaniumRangePoint allParticipantCrsConsensusPrice) {
    this.allParticipantCrsConsensusPrice = allParticipantCrsConsensusPrice;
  }


  public TitaniumConsensusExplorerRangeData bimodalLeftMean(TitaniumRangePoint bimodalLeftMean) {
    
    this.bimodalLeftMean = bimodalLeftMean;
    return this;
  }

   /**
   * Get bimodalLeftMean
   * @return bimodalLeftMean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getBimodalLeftMean() {
    return bimodalLeftMean;
  }


  public void setBimodalLeftMean(TitaniumRangePoint bimodalLeftMean) {
    this.bimodalLeftMean = bimodalLeftMean;
  }


  public TitaniumConsensusExplorerRangeData bimodalRightMean(TitaniumRangePoint bimodalRightMean) {
    
    this.bimodalRightMean = bimodalRightMean;
    return this;
  }

   /**
   * Get bimodalRightMean
   * @return bimodalRightMean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getBimodalRightMean() {
    return bimodalRightMean;
  }


  public void setBimodalRightMean(TitaniumRangePoint bimodalRightMean) {
    this.bimodalRightMean = bimodalRightMean;
  }


  public TitaniumConsensusExplorerRangeData challengeOverlayCrsConsensusPrice(TitaniumRangePoint challengeOverlayCrsConsensusPrice) {
    
    this.challengeOverlayCrsConsensusPrice = challengeOverlayCrsConsensusPrice;
    return this;
  }

   /**
   * Get challengeOverlayCrsConsensusPrice
   * @return challengeOverlayCrsConsensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getChallengeOverlayCrsConsensusPrice() {
    return challengeOverlayCrsConsensusPrice;
  }


  public void setChallengeOverlayCrsConsensusPrice(TitaniumRangePoint challengeOverlayCrsConsensusPrice) {
    this.challengeOverlayCrsConsensusPrice = challengeOverlayCrsConsensusPrice;
  }


  public TitaniumConsensusExplorerRangeData chartRanges(TitaniumChartRanges chartRanges) {
    
    this.chartRanges = chartRanges;
    return this;
  }

   /**
   * Get chartRanges
   * @return chartRanges
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumChartRanges getChartRanges() {
    return chartRanges;
  }


  public void setChartRanges(TitaniumChartRanges chartRanges) {
    this.chartRanges = chartRanges;
  }


  public TitaniumConsensusExplorerRangeData evpMid(TitaniumRangePoint evpMid) {
    
    this.evpMid = evpMid;
    return this;
  }

   /**
   * Get evpMid
   * @return evpMid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getEvpMid() {
    return evpMid;
  }


  public void setEvpMid(TitaniumRangePoint evpMid) {
    this.evpMid = evpMid;
  }


  public TitaniumConsensusExplorerRangeData expertPostChallengeConsensusPrice(TitaniumRangePoint expertPostChallengeConsensusPrice) {
    
    this.expertPostChallengeConsensusPrice = expertPostChallengeConsensusPrice;
    return this;
  }

   /**
   * Get expertPostChallengeConsensusPrice
   * @return expertPostChallengeConsensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getExpertPostChallengeConsensusPrice() {
    return expertPostChallengeConsensusPrice;
  }


  public void setExpertPostChallengeConsensusPrice(TitaniumRangePoint expertPostChallengeConsensusPrice) {
    this.expertPostChallengeConsensusPrice = expertPostChallengeConsensusPrice;
  }


  public TitaniumConsensusExplorerRangeData expertPreChallengeConsensusPrice(TitaniumRangePoint expertPreChallengeConsensusPrice) {
    
    this.expertPreChallengeConsensusPrice = expertPreChallengeConsensusPrice;
    return this;
  }

   /**
   * Get expertPreChallengeConsensusPrice
   * @return expertPreChallengeConsensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getExpertPreChallengeConsensusPrice() {
    return expertPreChallengeConsensusPrice;
  }


  public void setExpertPreChallengeConsensusPrice(TitaniumRangePoint expertPreChallengeConsensusPrice) {
    this.expertPreChallengeConsensusPrice = expertPreChallengeConsensusPrice;
  }


  public TitaniumConsensusExplorerRangeData marketDataCrsConsensusPrice(TitaniumRangePoint marketDataCrsConsensusPrice) {
    
    this.marketDataCrsConsensusPrice = marketDataCrsConsensusPrice;
    return this;
  }

   /**
   * Get marketDataCrsConsensusPrice
   * @return marketDataCrsConsensusPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getMarketDataCrsConsensusPrice() {
    return marketDataCrsConsensusPrice;
  }


  public void setMarketDataCrsConsensusPrice(TitaniumRangePoint marketDataCrsConsensusPrice) {
    this.marketDataCrsConsensusPrice = marketDataCrsConsensusPrice;
  }


  public TitaniumConsensusExplorerRangeData submissionMeanPoint(TitaniumRangePoint submissionMeanPoint) {
    
    this.submissionMeanPoint = submissionMeanPoint;
    return this;
  }

   /**
   * Get submissionMeanPoint
   * @return submissionMeanPoint
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getSubmissionMeanPoint() {
    return submissionMeanPoint;
  }


  public void setSubmissionMeanPoint(TitaniumRangePoint submissionMeanPoint) {
    this.submissionMeanPoint = submissionMeanPoint;
  }


  public TitaniumConsensusExplorerRangeData submissionPoint(TitaniumRangePoint submissionPoint) {
    
    this.submissionPoint = submissionPoint;
    return this;
  }

   /**
   * Get submissionPoint
   * @return submissionPoint
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumRangePoint getSubmissionPoint() {
    return submissionPoint;
  }


  public void setSubmissionPoint(TitaniumRangePoint submissionPoint) {
    this.submissionPoint = submissionPoint;
  }


  public TitaniumConsensusExplorerRangeData tradePeriodsWithMetrics(TitaniumTradePeriodsWithMetrics tradePeriodsWithMetrics) {
    
    this.tradePeriodsWithMetrics = tradePeriodsWithMetrics;
    return this;
  }

   /**
   * Get tradePeriodsWithMetrics
   * @return tradePeriodsWithMetrics
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumTradePeriodsWithMetrics getTradePeriodsWithMetrics() {
    return tradePeriodsWithMetrics;
  }


  public void setTradePeriodsWithMetrics(TitaniumTradePeriodsWithMetrics tradePeriodsWithMetrics) {
    this.tradePeriodsWithMetrics = tradePeriodsWithMetrics;
  }


  public TitaniumConsensusExplorerRangeData tradeRangesData(TitaniumTradeRangesData tradeRangesData) {
    
    this.tradeRangesData = tradeRangesData;
    return this;
  }

   /**
   * Get tradeRangesData
   * @return tradeRangesData
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumTradeRangesData getTradeRangesData() {
    return tradeRangesData;
  }


  public void setTradeRangesData(TitaniumTradeRangesData tradeRangesData) {
    this.tradeRangesData = tradeRangesData;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumConsensusExplorerRangeData titaniumConsensusExplorerRangeData = (TitaniumConsensusExplorerRangeData) o;
    return Objects.equals(this.allParticipantCrsConsensusPrice, titaniumConsensusExplorerRangeData.allParticipantCrsConsensusPrice) &&
        Objects.equals(this.bimodalLeftMean, titaniumConsensusExplorerRangeData.bimodalLeftMean) &&
        Objects.equals(this.bimodalRightMean, titaniumConsensusExplorerRangeData.bimodalRightMean) &&
        Objects.equals(this.challengeOverlayCrsConsensusPrice, titaniumConsensusExplorerRangeData.challengeOverlayCrsConsensusPrice) &&
        Objects.equals(this.chartRanges, titaniumConsensusExplorerRangeData.chartRanges) &&
        Objects.equals(this.evpMid, titaniumConsensusExplorerRangeData.evpMid) &&
        Objects.equals(this.expertPostChallengeConsensusPrice, titaniumConsensusExplorerRangeData.expertPostChallengeConsensusPrice) &&
        Objects.equals(this.expertPreChallengeConsensusPrice, titaniumConsensusExplorerRangeData.expertPreChallengeConsensusPrice) &&
        Objects.equals(this.marketDataCrsConsensusPrice, titaniumConsensusExplorerRangeData.marketDataCrsConsensusPrice) &&
        Objects.equals(this.submissionMeanPoint, titaniumConsensusExplorerRangeData.submissionMeanPoint) &&
        Objects.equals(this.submissionPoint, titaniumConsensusExplorerRangeData.submissionPoint) &&
        Objects.equals(this.tradePeriodsWithMetrics, titaniumConsensusExplorerRangeData.tradePeriodsWithMetrics) &&
        Objects.equals(this.tradeRangesData, titaniumConsensusExplorerRangeData.tradeRangesData);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allParticipantCrsConsensusPrice, bimodalLeftMean, bimodalRightMean, challengeOverlayCrsConsensusPrice, chartRanges, evpMid, expertPostChallengeConsensusPrice, expertPreChallengeConsensusPrice, marketDataCrsConsensusPrice, submissionMeanPoint, submissionPoint, tradePeriodsWithMetrics, tradeRangesData);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumConsensusExplorerRangeData {\n");
    sb.append("    allParticipantCrsConsensusPrice: ").append(toIndentedString(allParticipantCrsConsensusPrice)).append("\n");
    sb.append("    bimodalLeftMean: ").append(toIndentedString(bimodalLeftMean)).append("\n");
    sb.append("    bimodalRightMean: ").append(toIndentedString(bimodalRightMean)).append("\n");
    sb.append("    challengeOverlayCrsConsensusPrice: ").append(toIndentedString(challengeOverlayCrsConsensusPrice)).append("\n");
    sb.append("    chartRanges: ").append(toIndentedString(chartRanges)).append("\n");
    sb.append("    evpMid: ").append(toIndentedString(evpMid)).append("\n");
    sb.append("    expertPostChallengeConsensusPrice: ").append(toIndentedString(expertPostChallengeConsensusPrice)).append("\n");
    sb.append("    expertPreChallengeConsensusPrice: ").append(toIndentedString(expertPreChallengeConsensusPrice)).append("\n");
    sb.append("    marketDataCrsConsensusPrice: ").append(toIndentedString(marketDataCrsConsensusPrice)).append("\n");
    sb.append("    submissionMeanPoint: ").append(toIndentedString(submissionMeanPoint)).append("\n");
    sb.append("    submissionPoint: ").append(toIndentedString(submissionPoint)).append("\n");
    sb.append("    tradePeriodsWithMetrics: ").append(toIndentedString(tradePeriodsWithMetrics)).append("\n");
    sb.append("    tradeRangesData: ").append(toIndentedString(tradeRangesData)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("allParticipantCrsConsensusPrice");
    openapiFields.add("bimodalLeftMean");
    openapiFields.add("bimodalRightMean");
    openapiFields.add("challengeOverlayCrsConsensusPrice");
    openapiFields.add("chartRanges");
    openapiFields.add("evpMid");
    openapiFields.add("expertPostChallengeConsensusPrice");
    openapiFields.add("expertPreChallengeConsensusPrice");
    openapiFields.add("marketDataCrsConsensusPrice");
    openapiFields.add("submissionMeanPoint");
    openapiFields.add("submissionPoint");
    openapiFields.add("tradePeriodsWithMetrics");
    openapiFields.add("tradeRangesData");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumConsensusExplorerRangeData
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumConsensusExplorerRangeData.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumConsensusExplorerRangeData is not found in the empty JSON string", TitaniumConsensusExplorerRangeData.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumConsensusExplorerRangeData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumConsensusExplorerRangeData` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      // validate the optional field `allParticipantCrsConsensusPrice`
      if (jsonObj.getAsJsonObject("allParticipantCrsConsensusPrice") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("allParticipantCrsConsensusPrice"));
      }
      // validate the optional field `bimodalLeftMean`
      if (jsonObj.getAsJsonObject("bimodalLeftMean") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("bimodalLeftMean"));
      }
      // validate the optional field `bimodalRightMean`
      if (jsonObj.getAsJsonObject("bimodalRightMean") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("bimodalRightMean"));
      }
      // validate the optional field `challengeOverlayCrsConsensusPrice`
      if (jsonObj.getAsJsonObject("challengeOverlayCrsConsensusPrice") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("challengeOverlayCrsConsensusPrice"));
      }
      // validate the optional field `chartRanges`
      if (jsonObj.getAsJsonObject("chartRanges") != null) {
        TitaniumChartRanges.validateJsonObject(jsonObj.getAsJsonObject("chartRanges"));
      }
      // validate the optional field `evpMid`
      if (jsonObj.getAsJsonObject("evpMid") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("evpMid"));
      }
      // validate the optional field `expertPostChallengeConsensusPrice`
      if (jsonObj.getAsJsonObject("expertPostChallengeConsensusPrice") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("expertPostChallengeConsensusPrice"));
      }
      // validate the optional field `expertPreChallengeConsensusPrice`
      if (jsonObj.getAsJsonObject("expertPreChallengeConsensusPrice") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("expertPreChallengeConsensusPrice"));
      }
      // validate the optional field `marketDataCrsConsensusPrice`
      if (jsonObj.getAsJsonObject("marketDataCrsConsensusPrice") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("marketDataCrsConsensusPrice"));
      }
      // validate the optional field `submissionMeanPoint`
      if (jsonObj.getAsJsonObject("submissionMeanPoint") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("submissionMeanPoint"));
      }
      // validate the optional field `submissionPoint`
      if (jsonObj.getAsJsonObject("submissionPoint") != null) {
        TitaniumRangePoint.validateJsonObject(jsonObj.getAsJsonObject("submissionPoint"));
      }
      // validate the optional field `tradePeriodsWithMetrics`
      if (jsonObj.getAsJsonObject("tradePeriodsWithMetrics") != null) {
        TitaniumTradePeriodsWithMetrics.validateJsonObject(jsonObj.getAsJsonObject("tradePeriodsWithMetrics"));
      }
      // validate the optional field `tradeRangesData`
      if (jsonObj.getAsJsonObject("tradeRangesData") != null) {
        TitaniumTradeRangesData.validateJsonObject(jsonObj.getAsJsonObject("tradeRangesData"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumConsensusExplorerRangeData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumConsensusExplorerRangeData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumConsensusExplorerRangeData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumConsensusExplorerRangeData.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumConsensusExplorerRangeData>() {
           @Override
           public void write(JsonWriter out, TitaniumConsensusExplorerRangeData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumConsensusExplorerRangeData read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumConsensusExplorerRangeData given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumConsensusExplorerRangeData
  * @throws IOException if the JSON string is invalid with respect to TitaniumConsensusExplorerRangeData
  */
  public static TitaniumConsensusExplorerRangeData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumConsensusExplorerRangeData.class);
  }

 /**
  * Convert an instance of TitaniumConsensusExplorerRangeData to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

